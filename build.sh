#!/bin/bash

# Install the dependencies for the project
pip install -r requirements.txt

# Run Django's collectstatic command to gather all static files
python manage.py collectstatic --noinput

# Run Django's migrate command to apply any outstanding database migrations
python manage.py migrate

python manage.py createsuperuser --noinput --username ayush --email ayushkr1701@gmail.com --password Abhay@123

# Start the Django development server
# gunicorn config.wsgi

