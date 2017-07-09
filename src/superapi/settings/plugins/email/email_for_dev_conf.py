#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = True
SERVER_EMAIL = os.getenv("SERVER_EMAIL")
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
NOTICE_EMAIL_LIST = [EMAIL_HOST]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_USE_SSL =""
