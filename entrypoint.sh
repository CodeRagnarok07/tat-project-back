#!/bin/sh

echo 'Running collecstatic...'
python manage.py collectstatic --no-input

echo 'Running server...'
gunicorn config.wsgi:application --bind 0.0.0.0:8000