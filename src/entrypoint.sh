#!/bin/sh

# Wait for PostgreSQL start up to 
# collect static and run magrations
echo "Waiting for PostgreSQL..."
while ! nc -z $SQL_HOST $SQL_PORT; do
    sleep 0.1
done
echo "PostgreSQL started"

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

echo "Ready to run!"

exec "$@"
