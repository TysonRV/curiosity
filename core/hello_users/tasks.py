import string

from celery import Celery
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

app = Celery('hello_users', broker=settings.CELERY_BROKER_URL)


@app.task
def create_random_user_accounts(total):
    print("Creating users....")
    for i in range(total):
        username = 'user_{}'.format(get_random_string(10, string.ascii_letters))
        email = '{}@example.com'.format(username)
        password = get_random_string(50)
        User.objects.create_user(username=username, email=email, password=password)
    return '{} random users created with success!'.format(total)
