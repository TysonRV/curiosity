#!/usr/bin/env python

import os
import sys
import yaml

from django.core.management import execute_from_command_line

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.base")

    if 'test' in sys.argv:
        os.environ.setdefault("ENV", "TEST")
    else:
        os.environ.setdefault("ENV", "DEV")

    if os.path.isfile('env.yml'):
        env_vars = yaml.load(open('env.yml').read(), Loader=yaml.FullLoader)

        for key, value in env_vars[os.getenv('ENV')].items():
            os.environ.setdefault(key, value)
    execute_from_command_line(sys.argv)
