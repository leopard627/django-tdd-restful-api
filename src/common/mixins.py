from django.http.response import Http404
from django.utils import timezone

from rest_framework import mixins, status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.settings import api_settings


class NestedViewSetMixin(object):
    parent = None
    parent_lookup_field = 'nested'

    def get_nested_filter_dict(self):
        filter_dict = {}
        if not self.parent:
            return filter_dict
        viewset = self.parent(request=self.request)
        if isinstance(viewset, NestedViewSetMixin):
            filter_dict.update(viewset.get_nested_filter_dict())

        filter_dict.update({self.parent_lookup_field: self.kwargs.get('%s_%s' % (self.parent_lookup_field, viewset.lookup_field))})
        return filter_dict

    def get_queryset(self):
        return super(NestedViewSetMixin, self).get_queryset().filter(**self.get_nested_filter_dict())

    def perform_create(self, serializer):
        viewset = self.parent(request=self.request, kwargs={self.parent.lookup_field: self.get_nested_filter_dict().get(self.parent_lookup_field)})
        serializer.save(**{self.parent_lookup_field: viewset.get_object()})

    def get_success_headers(self, data):
        try:
            return {'Location': data[api_settings.URL_FIELD_NAME]}
        except (TypeError, KeyError):
            return {}


class NestedCreateModelMixin(NestedViewSetMixin):

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        viewset = self.parent(
            request=self.request,
            kwargs={
                self.parent.lookup_field: self.get_nested_filter_dict().get(self.parent_lookup_field)
            })

        serializer.save(**{self.parent_lookup_field: viewset.get_object()})

    def get_success_headers(self, data):
        try:
            return {'Location': data[api_settings.URL_FIELD_NAME]}
        except (TypeError, KeyError):
            return {}


class DeleteMixin(object):
    def perform_destroy(self, instance):
        instance.deleted_at = timezone.now()
        instance.save()
