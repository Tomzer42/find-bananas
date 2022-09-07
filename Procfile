web: gunicorn django_find_bananas.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate