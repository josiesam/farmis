#!/bin/bash -x

echo "Waiting for postgres..."

while ! nc -z $POSTGRESQL_HOST $POSTGRESQL_PORT; do
    sleep 0.5
done
echo "PostgreSQL started!!!"

while ! nc -z $REDIS_HOST $REDIS_PORT; do
    sleep 0.5
done
echo "Redis started!!!"


python manage.py makemigrations --noinput || exit 1
python manage.py migrate --noinput || exit 1
exec "$@"