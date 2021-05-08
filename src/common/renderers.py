import time
from rest_framework.renderers import JSONRenderer
from django.shortcuts import resolve_url
from django.template.loader import render_to_string
from django.utils.encoding import force_str
from django.utils.functional import Promise
from rest_framework.renderers import BaseRenderer, JSONRenderer, TemplateHTMLRenderer
from rest_framework.utils import encoders, json

# from drf_yasg.app_settings import redoc_settings, swagger_settings
# from drf_yasg.codecs import VALIDATORS, OpenAPICodecJson, OpenAPICodecYaml
# from drf_yasg.openapi import Swagger
# from drf_yasg.utils import filter_none

class AwesomeJSONRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        status_code = renderer_context['response'].status_code

        # {'detail': ErrorDetail(string='address value is not Bitcoin Address or Web Address', code='00002')}
        if 'detail' in data:
            # 에러 exception 인경우임
            message = str(data['detail'])
            message_code = int(data['detail'].code)
            response = {
                # 'timnestamp': int(time.time()),
                # 'success': True,
                # 'status_code': status_code,
                'message_code': message_code,
                'message': message,
                'data': None,
                # 'status_code': 200, # 200 고정임
                # 'result': {
                #     'msg': '',
                #     'msg_code': '200',
                #     'data': data,
                # },
                # 'error': message,
                # 'error_code': message_code,
            }

        elif ('detail' not in data) and (status_code in [200, 201, 202]):
            response = {
                # 'timnestamp': int(time.time()),
                # 'success': True,
                # 'status_code': status_code,
                'message_code': 100,
                'message': 'success',
                'data': data,
                # 'status_code': 200, # 200 고정임
                # 'result': {
                #     'msg': '',
                #     'msg_code': '200',
                #     'data': data,
                # },
                # 'error': '',
                # 'error_code': '',
            }
        else:
            # 기본 400 에러인경우
            response = {
                # 'timnestamp': int(time.time()),
                # 'success': True,
                # 'status_code': status_code,
                'message_code': status_code,
                'message': data,
                'data': None,
                # 'status_code': 200, # 200 고정임
                # 'result': {
                #     'msg': '',
                #     'msg_code': '200',
                #     'data': data,
                # },
                # 'error': '',
                # 'error_code': '',
            }

        return super(AwesomeJSONRenderer, self).render(response, accepted_media_type, renderer_context)


