#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from django.contrib.auth.models import User

from posts.models import Post


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'email',
            'is_active',
        )


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'
