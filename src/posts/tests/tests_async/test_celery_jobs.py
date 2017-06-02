#!/usr/bin/env python
# -*- coding: utf-8 -*-


from posts.tasks import world
from posts.tests.base import PostsBaseTest


class TestCeleryTasks(PostsBaseTest):

    def test_celery_tasks_module_level_test(self):
        res = world.delay(1000)

        # .get() 으로 리턴값을 확인 할 수 있습니다.
        assert res.get() == 1000
        assert res.successful() == True
