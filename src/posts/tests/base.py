#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.test import TestCase

# 한글로 주석 쓰려고 맨위에 저런걸 달아요


class PostsBaseTest(TestCase):

    def test_create_user_model(self):
        User.objects.create(
                username='Hello_World'
        )
        assert User.objects.count() == 1, "Should be equal"
