#!/bin/bash

# Install requirements from requirement.txt
pip install -r requirements.txt

# Create migrations (assuming Django project structure)
python manage.py makemigrations --no-input

# Apply migrations to the database
python manage.py migrate --no-input

# Collect staticfiles 
python manage.py collectstatic --no-input --clear

# Create a superuser with credentials from environment variables
python manage.py createsuperuser \
  --email "$SUPERUSER_EMAIL" \
  --password "$SUPERUSER_PASSWORD" \
  --no-input
