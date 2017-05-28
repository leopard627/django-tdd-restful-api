#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .base import *

OPTIONAL_APPS = [
        'django_extensions',
]

INSTALLED_APPS = PREQ_APPS + PROJECT_APPS + OPTIONAL_APPS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}
