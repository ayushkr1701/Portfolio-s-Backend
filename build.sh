#!/bin/bash

# Install the dependencies for the project
pip install -r requirements.txt

# Run Django's collectstatic command to gather all static files
python manage.py collectstatic --noinput

# Run Django's migrate command to apply any outstanding database migrations
python manage.py migrate

DJANGO_SUPERUSER_EMAIL=xxx@email.com
export DJANGO_SUPERUSER_EMAIL

DJANGO_SUPERUSER_USERNAME=xxx
export DJANGO_SUPERUSER_USERNAME

DJANGO_SUPERUSER_PASSWORD=xxx
export DJANGO_SUPERUSER_PASSWORD



python manage.py createsuperuser --username $DJANGO_SUPERUSER_USERNAME 

# Start the Django development server
# gunicorn config.wsgi

