from __future__ import absolute_import
from posts.celery import app


@app.task
def world(num):
    for x in range(5):
        print("************I dont wanna night-shift work*******")
    return num


@app.task
def callable_task():
    for x in range(5):
        print("------------------spawn by user-------------------")
