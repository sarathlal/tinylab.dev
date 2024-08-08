---
layout: post
title:  How to Create a Django Application with the Latest Versions of Python, Django, PostgreSQL, and Docker
categories: jekyll update
description: Learn how to create a Django application with the latest versions of Python, Django, and PostgreSQL using Docker. This beginner-friendly guide includes step-by-step instructions, best practices for managing environment variables, and accessing the Django admin interface. Perfect for developers looking to set up a robust and consistent development environment.
---

Creating a Django application using Docker is a great way to ensure a consistent and isolated environment for development. This guide will take you through setting up a Django project with the latest versions of Python, Django, and PostgreSQL. We’ll also cover using environment variables to securely manage database credentials. By the end of this guide, you'll have a functional Django application and be ready to explore and expand it further.

Starting this project will not only help you learn essential skills but also provide a robust foundation for developing modern web applications. Let's dive in!

## Setting Up the Project Directory

First, we need to create a new directory for our project and navigate into it:

```bash
mkdir dockerdjango
cd dockerdjango
```

This command creates a new directory named `dockerdjango` and moves into it. This directory will hold all the files and configurations for your Django project.

## Creating the Dockerfile

Next, we’ll create a `Dockerfile` in the project directory. This file will define the Docker image for your Django project:

```Dockerfile
# Use the official Python image from the Docker Hub
FROM python:latest

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the project files to the working directory
COPY . /code/
```

Here's what this file does:
- `FROM python:latest`: Uses the latest Python image as the base for your container.
- `ENV PYTHONDONTWRITEBYTECODE 1` and `ENV PYTHONUNBUFFERED 1`: These settings ensure Python won’t write `.pyc` files and that output is not buffered.
- `WORKDIR /code`: Sets the working directory inside the container to `/code`.
- `COPY requirements.txt /code/`: Copies the `requirements.txt` file into the container.
- `RUN pip install --upgrade pip` and `RUN pip install -r requirements.txt`: Upgrades `pip` and installs the dependencies.
- `COPY . /code/`: Copies all the files from your local directory to the container’s `/code/` directory.

## Creating the Requirements File

Now, create a `requirements.txt` file in the project directory. This file will list the Python packages needed for your project:

```txt
Django
psycopg2-binary
python-dotenv
```

This includes Django, the PostgreSQL adapter, and the `python-dotenv` package for loading environment variables from a `.env` file.

## Setting Up Docker Compose

To define our services, we need to create a `docker-compose.yml` file in the project directory:

```yaml
version: '3.8'

services:
  db:
    image: postgres:latest
    env_file:
      - .env.db
    volumes:
      - postgres_data:/var/lib/postgresql/data

  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/code
    ports:
      - "8000:8000"
    env_file:
      - .env.web
    depends_on:
      - db

volumes:
  postgres_data:
```

This file sets up two services:
- `db`: Uses the latest PostgreSQL image and loads environment variables from `.env.db`.
- `web`: Builds the image using the `Dockerfile`, runs the Django development server on port 8000, mounts the code directory for live reloading, and loads environment variables from `.env.web`. It also ensures the database starts first.

## Creating Environment Variable Files

Create a `.env.db` file for database environment variables:

```env
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
```

This file contains the settings for configuring PostgreSQL.

Next, create a `.env.web` file for Django environment variables:

```env
DEBUG=1
SECRET_KEY=your_secret_key
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=postgres
SQL_USER=postgres
SQL_PASSWORD=postgres
SQL_HOST=db
SQL_PORT=5432
```

This file includes settings for debugging, secret key, allowed hosts, and database connection details.

## Creating the Django Project

Build the Docker images and start the containers:

```bash
docker-compose up -d --build
```

This command builds the Docker images and starts the containers in detached mode.

Access the web container’s shell:

```bash
docker-compose exec web bash
```

This command opens a shell in the running `web` container.

Create a new Django project:

```bash
django-admin startproject dockerdjango .
```

This command creates a new Django project named `dockerdjango` in the current directory.

## Configuring Django to Use PostgreSQL

Modify `dockerdjango/settings.py` to use environment variables:

```python
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = os.getenv('DEBUG', '0') == '1'

ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS').split(' ')

DATABASES = {
    'default': {
        'ENGINE': os.getenv('SQL_ENGINE', 'django.db.backends.postgresql'),
        'NAME': os.getenv('SQL_DATABASE', BASE_DIR / 'db.sqlite3'),
        'USER': os.getenv('SQL_USER', 'user'),
        'PASSWORD': os.getenv('SQL_PASSWORD', 'password'),
        'HOST': os.getenv('SQL_HOST', 'localhost'),
        'PORT': os.getenv('SQL_PORT', '5432'),
    }
}
```

This modification ensures that Django loads configuration values from environment variables.

## Running Migrations and Creating a Superuser

Apply the migrations to create the necessary database tables:

```bash
python manage.py migrate
```

Create a superuser for the Django admin interface:

```bash
python manage.py createsuperuser
```

Follow the prompts to create a superuser account.

## Accessing the Django Admin Interface

To access the admin interface, open your web browser and navigate to `http://localhost:8000/admin`. Log in using the superuser credentials you created. You should see the Django admin dashboard, where you can manage your application’s data and settings.

---

By following this guide, you have successfully created a Django application with the latest versions of Python, Django, PostgreSQL, and Docker. This setup ensures a consistent development environment and makes it easy to manage dependencies and deploy your application. You're now ready to explore the powerful features of Django and Docker. If you have any questions or run into issues, feel free to ask in the comments!
