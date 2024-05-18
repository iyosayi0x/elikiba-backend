#!/bin/bash

# Install requirements from requirements.txt
pip install -r requirements.txt

# Create migrations (assuming Django project structure)
python manage.py makemigrations --no-input

# Apply migrations to the database
python manage.py migrate --no-input

# Collect staticfiles
python manage.py collectstatic --no-input --clear

# Create a superuser with credentials from environment variables
if [ -z "$SUPERUSER_EMAIL" ] || [ -z "$SUPERUSER_PASSWORD" ]; then
  echo "SUPERUSER_EMAIL and SUPERUSER_PASSWORD environment variables must be set."
  exit 0
fi

python manage.py shell <<EOF
from django.contrib.auth import get_user_model

User = get_user_model()
email = "$SUPERUSER_EMAIL"
password = "$SUPERUSER_PASSWORD"

if not User.objects.filter(email=email).exists():
    print("Creating supseruser")
    User.objects.create_superuser(email=email, password=password)
else:
    print("Superuser already exists")
EOF