#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from rest_framework import routers

from posts.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)


urlpatterns = [
        url(r'', include(router.urls))
]
