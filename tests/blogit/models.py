# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.utils.text import slugify

from blogit.models import Category


def create_category(name, parent=None):
    return Category.objects.create(name=name, slug=slugify(name), parent=None)


class TestCategory(TestCase):
    def setUp(self):
        self.cat_food = create_category('Food')

    def test_get_absolute_url(self):
        self.assertEquals(
            self.cat_food.get_absolute_url(), '/en/categories/food/')
