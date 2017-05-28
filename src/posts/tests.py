#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.test import TestCase

# 한글로 주석 쓰려고 맨위에 저런걸 달아요


class TestPostsTest(TestCase):

    def test_smoke_test(self):
        assert 1 is not 1, "당연히 같아야해요"
