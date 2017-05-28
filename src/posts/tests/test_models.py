#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth.models import User

import pytest
from mixer.backend.django import mixer

from .base import PostsBaseTest

# 한글로 주석 쓰려고 맨위에 저런걸 달아요
pytestmark = pytest.mark.django_db


class PostViewTests(PostsBaseTest):
    def test_create_user_model(self):
        User.objects.create(username='Hello_World')
        assert User.objects.count() == 1, "Should be equal"

    def test_create_suuser_via_mixer(self):
        super_user = mixer.blend('auth.User', is_staff=True, is_superuser=True)
        assert User.objects.count() is 1, 'Should be equal'
        assert super_user.is_superuser is True, 'Should be superuser'

    def test_create_user_via_mixer(self):
        for cnt in range(50):
            mixer.blend('auth.User')
        assert User.objects.count() == 50, 'Should be equal'
