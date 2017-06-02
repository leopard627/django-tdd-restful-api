#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import

import os
import djcelery
from datetime import timedelta

djcelery.setup_loader()

# 만약에 RABBITMQ_HOST가 없다면 , 옆에 디폴트로 로컬 것을 가져옵니다.
BROKER_URL = os.environ.get('RABBITMQ_HOST', "amqp://guest@localhost//")

CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
CELERY_RESULT_BACKEND = 'djcelery.backends.database:DatabaseBackend'

CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CELERYBEAT_SCHEDULE = {
    'periodic_tasks': {
          'task': 'posts.tasks.world',
          'schedule': timedelta(seconds=10),
    }
}
