#!/bin/sh

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Applying database migrations..."
python manage.py migrate

echo "Ready to run!"

exec "$@"
