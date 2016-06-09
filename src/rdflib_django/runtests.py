# This file mainly exists to allow python setup.py test to work.

import django
import os, sys

from django.test.utils import get_runner
from django.conf import settings


def configure():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rdflib_django.testsettings')
    django.setup()

def runtests():
    TestRunner = get_runner(settings)
    test_runner = TestRunner(verbosity=1, interactive=True)
    failures = test_runner.run_tests(['rdflib_django'])
    sys.exit(bool(failures))


configure()

if __name__ == '__main__':
    runtests()
