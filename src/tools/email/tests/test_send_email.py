 #!/usr/bin/env python
# -*- coding: utf-8 -*-


import pytest

from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.test import TestCase

from django.core import mail

from oauth2_provider.models import get_application_model, AccessToken
from oauth2_provider.tests.test_utils import TestCaseUtils
from rest_framework import status
from mixer.backend.django import mixer

from rest_framework.test import APITestCase

Application = get_application_model()
pytestmark = pytest.mark.django_db


class TestSendEmaiTest(TestCase):

    def test_send_super_simple_email_to_me(self):
        send_mail(
            'Subject here',
            'Here is the message.',
            'elastic7327@gmail.com',  # from
            ['jhe7327@naver.com', 'jhkim@dibiup.com', 'elastic7327@gmail.com'],  # to
            fail_silently=True,
        )
        assert len(mail.outbox) == 1
        assert mail.outbox[0].subject == 'Subject here'

    def test_send_email_message(self):
        msg = EmailMessage('Request Callback', 'Here is the message.', to=['jhe7327@naver.com', 'elastic7327gmail.com', 'jhkim@dibiup.com'])
        msg.send()
