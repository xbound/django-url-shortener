#!/bin/bash -x

python manage.py migrate --noinput || exit 1
python manage.py create_default_admin
python manage.py runserver 0.0.0.0:8000