#!/bin/bash

# Install the dependencies for the project
pip install -r requirements.txt

# Run Django's collectstatic command to gather all static files
python manage.py collectstatic --noinput

# Run Django's migrate command to apply any outstanding database migrations
python manage.py migrate
$export DJANGO_SUPERUSER_EMAIL= ayushkr1701@gmail.com
$export DJANGO_SUPERUSER_USERNAME= ayushkr1701
$export DJANGO_SUPERUSER_PASSWORD= Abhay@123



python manage.py createsuperuser --noinput 

# Start the Django development server
# gunicorn config.wsgi

