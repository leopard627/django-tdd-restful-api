#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .base import *

OPTIONAL_APPS = [
        'django_extensions',
]


# Celery를 테스트모드에서 실행할때에 꼭..
CELERY_ALWAYS_EAGER = True
TEST_RUNNER = 'djcelery.contrib.test_runner.CeleryTestSuiteRunner'

INSTALLED_APPS = PREQ_APPS + PROJECT_APPS + OPTIONAL_APPS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}
