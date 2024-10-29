#!/bin/sh

yes | python manage.py migrate
python manage.py collectstatic --noinput

echo "The ENVIRONMENT variable is not set to LOCAL"
gunicorn inventory_management.wsgi:application -b 0.0.0.0:8000 --reload --timeout=300 --workers 5 --thread=100 --access-logfile=- --error-logfile=-