#!/bin/bash
docker exec -i thundersite-django python manage.py makemigrations
docker exec -i thundersite-django python manage.py migrate
docker exec -i thundersite-django python manage.py loaddata ./scripts/db/seed.json
