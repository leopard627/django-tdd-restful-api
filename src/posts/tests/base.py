"""
File: base.py
Author: Me
Email: yourname@email.com
Github: https://github.com/yourname
Description:
"""

from datetime import timedelta

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.utils.crypto import get_random_string

from rest_framework.test import APITestCase
# from oauth2_provider.tests.test_utils import TestCaseUtils
from oauth2_provider.models import get_application_model, AccessToken
from rest_framework import status

import json
import pytest
from mixer.backend.django import mixer

Application = get_application_model()
pytestmark = pytest.mark.django_db


class PostsBaseTest(APITestCase):

    def test_create_user_model(self):
        User.objects.create(
                username='Hello_World'
        )
        assert User.objects.count() == 1, "Should be equal"

    def set_oauth2_app_by_admin(self, user):
        app = Application.objects.create(
                name='SuperAPI OAUTH2 APP',
                user=user,
                client_type=Application.CLIENT_PUBLIC,
                authorization_grant_type=Application.GRANT_PASSWORD,
        )
        return app

    def get_token(self, access_user, app):
        random = get_random_string(length=1024)
        access_token = AccessToken.objects.create(
                user=access_user,
                scope='read write',
                expires=timezone.now() + timedelta(minutes=5),
                token=f'{random}---{access_user.username}',
                application=app
        )
        return access_token.token
