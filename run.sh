#!/bin/bash
cd app
python manage.py migrate
gunicorn src.wsgi
