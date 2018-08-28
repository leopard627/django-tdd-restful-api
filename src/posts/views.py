from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import viewsets
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope

from posts.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [TokenHasReadWriteScope]
    serializer_class = UserSerializer
    queryset = User.objects.all()
