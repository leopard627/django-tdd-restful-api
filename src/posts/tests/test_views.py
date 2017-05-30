#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import timedelta

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.utils.crypto import get_random_string

from oauth2_provider.models import get_application_model, AccessToken
from rest_framework import status

import json
import pytest
from mixer.backend.django import mixer


from .base import PostsBaseTest

Application = get_application_model()
pytestmark = pytest.mark.django_db


class PostViewsTests(PostsBaseTest):

    def test_create_fake_data_then_send_get_request_via_user_viewset(self):
        admin_user = mixer.blend('auth.User', is_staff=True, is_superuser=True)
        app = Application.objects.create(
                name='SuperAPI OAUTH2 APP',
                user=admin_user,
                client_type=Application.CLIENT_PUBLIC,
                authorization_grant_type=Application.GRANT_PASSWORD,
        )
        assert Application.objects.count() == 1, "Should be equal"

        random = get_random_string(length=16)

        admin_token = AccessToken.objects.create(
                user=admin_user,
                scope='read write',
                # 조금 까다롭네요 . . .
                expires=timezone.now() + timedelta(minutes=5),
                token=f'{random}---{admin_user.username}',
                application=app
        )

        for cnt in range(50):
            mixer.blend('auth.User', is_active=True)

        url = reverse('user-list')

        # 이 부분이 포인트 입니다.
        self.client.credentials(
                HTTP_AUTHORIZATION=f'Bearer {admin_token.token}'
        )
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK

    def test_send_get_request_via_user_viewset(self):
        # list   GET : POST
        # retrive / patch / des /  GET:PUT:DELETE
        admin_user = mixer.blend(
                'auth.User',
                is_staff=True,
                is_superuser=True)

        app = self.set_oauth2_app_by_admin(admin_user)
        access_token = self.get_token(admin_user, app)

        url = reverse('user-list')
        self.client.credentials(
                HTTP_AUTHORIZATION=f'Bearer {access_token}'
        )
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK

    def test_send_post_request_via_user_viewset(self):
        # list   GET : POST
        # retrive / patch / des /  GET:PUT:DELETE

        admin_user = mixer.blend(
                'auth.User',
                is_staff=True,
                is_superuser=True)

        app = self.set_oauth2_app_by_admin(admin_user)
        access_token = self.get_token(admin_user, app)

        url = reverse('user-list')
        data = {
            'username': 'HiDaniel',
            'password': 'Hello_Ela',
            'email': 'elastic7327@gmail.com',
            'is_active': True,
        }

        self.client.credentials(
                HTTP_AUTHORIZATION=f'Bearer {access_token}'
        )
        response = self.client.post(url, data=data, format='json')
        print(response.content)
        assert response.status_code == status.HTTP_201_CREATED

    def test_send_retrive_update_destroy_request_via_user_viewset(self):

        admin_user = mixer.blend(
                'auth.User',
                is_staff=True,
                is_superuser=True)

        app = self.set_oauth2_app_by_admin(admin_user)
        access_token = self.get_token(admin_user, app)

        # POST 를 이용해서 유져생성
        url = reverse('user-list')
        data = {
            'username': 'HiDaniel',
            'password': 'Hello_Ela',
            'email': 'elastic7327@gmail.com',
            'is_active': True,
        }

        self.client.credentials(
                HTTP_AUTHORIZATION=f'Bearer {access_token}'
        )
        response = self.client.post(url, data=data, format='json')
        assert response.status_code == status.HTTP_201_CREATED

        url = reverse('user-detail', args=[1])

        # 여기서 토큰을 다시 넣을 필요가 없는 이유는
        # 위에서 부터 쭉 세션이 이어지기 때문입니다.
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK

        url = reverse('user-detail', args=[1])
        data = {
            'is_active': False,
        }

        # 이곳 역시 토큰을 다시 넣을 필요가 없는 이유는
        # 위에서 부터 쭉 세션이 이어지기 때문입니다.

        response = self.client.patch(
                url,
                data=json.dumps(data),
                content_type='application/json'
        )
        print(response.content)
        assert response.status_code == status.HTTP_200_OK
