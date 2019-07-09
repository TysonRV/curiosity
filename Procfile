web: gunicorn core.wsgi --log-file -
main_worker: celery -A core worker -B -l INFO
