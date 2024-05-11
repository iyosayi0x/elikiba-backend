## Elikiba: A Django Backend for Article Management

**Elikiba** empowers you to effortlessly manage your articles through a user-friendly Django admin interface. Here's what you can achieve with Elikiba:

* **Seamless Article Creation:** Craft compelling articles directly within the Django admin panel. Elikiba provides a streamlined interface for adding, editing, and organizing your content.
* **Docker-powered Deployment:** Leverage the efficiency of Docker containers for deploying Elikiba. This streamlined approach simplifies the setup process and ensures consistent execution across environments.

**Getting Started**

To embark on your Elikiba journey, follow these steps:

1. **Project Setup:**

```sh
git clone git@github.com:iyosayi0x/elikiba-backend.git
cd elikiba

# setup virtual environment 
python3 -m virtualenv venv 

# install requirements.txt 
pip install -r requirements.txt
```

2. **Database Configuration:**

- Update `settings.py` with your database credentials. Refer to the Django documentation for guidance on database configuration: [https://docs.djangoproject.com/en/5.0/](https://docs.djangoproject.com/en/5.0/)

3. **Migrations and Admin:**

```sh
python manage.py migrate
python manage.py createsuperuser
```

4. **Docker (Optional):**

```sh
# Build the docker image 
docker-compose build

# Run the docker image
docker-compose up
```

