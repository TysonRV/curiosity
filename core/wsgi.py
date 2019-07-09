"""
WSGI config for curiosity project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import yaml

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("ENV", "PROD")

if os.path.isfile('env.yml'):
    env_vars = yaml.load(open('env.yml').read(), Loader=yaml.FullLoader)

    for key, value in env_vars[os.getenv('ENV')].items():
        os.environ.setdefault(key, value)

application = get_wsgi_application()
