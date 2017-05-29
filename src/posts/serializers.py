#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'email',
            'is_active',
        )
