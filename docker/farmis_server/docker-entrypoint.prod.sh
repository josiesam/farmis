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


# Create datbase if it doesn't exist
# PGPASSWORD=$POSTGRESQL_USER_PASSWORD psql -h $POSTGRESQL_HOST -U $POSTGRESQL_USER_NAME -d postgres -tc "SELECT 1 FROM pg_database WHERE datname = '$POSTGRESQL_DB_NAME'" | grep -q 1 || PGPASSWORD=$POSTGRESQL_USER_PASSWORD psql -h $POSTGRESQL
# Check if the database exists
if PGPASSWORD=$POSTGRESQL_USER_PASSWORD psql -h $POSTGRESQL_HOST -U $POSTGRESQL_USER_NAME -d postgres -tAc "SELECT 1 FROM pg_database WHERE datname = '$POSTGRESQL_DB_NAME'" | grep -q 1; then
    echo "Database $POSTGRESQL_DB_NAME already exists"
else
    echo "Database $POSTGRESQL_DB_NAME does not exist. Creating..."
    PGPASSWORD=$POSTGRESQL_USER_PASSWORD psql -h $POSTGRESQL_HOST -U $POSTGRESQL_USER_NAME -d postgres -c "CREATE DATABASE $POSTGRESQL_DB_NAME"
    echo "Database $POSTGRESQL_DB_NAME created successfully"
fi

python manage.py migrate --noinput || exit 1
# python manage.py collectstatic --noinput --clear || exit 1
exec "$@"