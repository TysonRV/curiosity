import os

import yaml
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

os.environ.setdefault("ENV", "DEV")

if os.path.isfile('env.yml'):
    env_vars = yaml.load(open('env.yml').read(), Loader=yaml.FullLoader)

    for key, value in env_vars[os.getenv('ENV')].items():
        os.environ.setdefault(key, value)

app = Celery('core')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
