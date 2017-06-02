#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 이 테스트는 반드시 development 에서 돌려야합니다.
# 그리고 테스트를 돌릴때는 아래처럼 TEST_RUNNER을 꼭 settings.py 에 기입을 해주세요
# TEST_RUNNER = 'djcelery.contrib.test_runner.CeleryTestSuiteRunner'

from posts.tasks import world

from posts.tests.base import PostsBaseTest


class TestCeleryTasks(PostsBaseTest):
    """
    Celery 테스트 설정관련 사항은 아래의 레퍼런스를 참조하시면
    좋습니다.

    http://docs.celeryproject.org/projects/django-celery/en/2.4/cookbook/unit-testing.html

    """
    def test_smoke_test(self):
        """Test that the ``add`` task runs with no errors,
        and returns the correct result."""
        result = world.delay(5)
        # result.get() 을 통해서
        # 비동기 처리할 함수의 리턴값을 가져올 수 있습니다.
        assert result.get() == 5
        # 또는 successful() 함수를 통해서
        # 성공 여부를 가져올 수 있습니다.
        assert result.successful() == True
