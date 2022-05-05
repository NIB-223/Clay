#!/usr/bin/env bash
python manage.py collectstatic --noinput
python manage.py migrate
uwsgi --ini /uwsgi.ini --env DJANGO_SETTINGS_MODULE=conf.settings
