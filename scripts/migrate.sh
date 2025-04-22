#!/bin/sh
echo 'Executando migrate.sh'
makemigrations.sh
python manage.py migrate --noinput
