#! /bin/bash
echo "Dejango deployment" && gunicorn --worker-tmp-dir /dev/shm django_app.wsgi && python3 manage.py migrate