#!/usr/bin/env python
# -*- coding: utf-8 -*-


REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
                'oauth2_provider.ext.rest_framework.OAuth2Authentication',
            )
        }
