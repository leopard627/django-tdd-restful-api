from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter, OrderingFilter

from rest_framework import viewsets
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope

from posts.serializers import UserSerializer, PostSerializer
from posts.models import Post

from common.paginations import RegularResultSetPagination


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [TokenHasReadWriteScope]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class PostViewSet(viewsets.ModelViewSet):
    __basic_fields = ('id', 'title', 'contents')
    permission_classes = [TokenHasReadWriteScope]
    pagination_class = RegularResultSetPagination
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = __basic_fields
    search_fields = __basic_fields
