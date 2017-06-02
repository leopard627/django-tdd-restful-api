#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from posts.celery import app


@app.task
def world(num):
    for x in range(num):
        print("**************진짜 퇴근좀 하자***************")
    return num


@app.task
def callable_task():
    for x in range(5):
        print("------------------spawn by user-------------------")
