#!/bin/sh
python manage.py migrate
python manage.py collectstatic --no-input
gunicorn --bind :8000 --workers 3 --reload bookstore.wsgi:application