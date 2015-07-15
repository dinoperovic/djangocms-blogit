# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.test import TestCase
from django.utils.text import slugify
from django.utils import timezone

from cms.api import add_plugin

from blogit.models import Category, Tag, Post
from blogit import settings as bs


def create_category(name, **kwargs):
    return Category.objects.create(name=name, slug=slugify(name), **kwargs)


def create_tag(name, **kwargs):
    return Tag.objects.create(name=name, slug=slugify(name), **kwargs)


def create_post(title, date=None, status=2, **kwargs):
    if date is None:
        date = timezone.now()
    else:
        date = timezone.make_aware(date, timezone.get_default_timezone())

    kwargs['description'] = title

    return Post.objects.create(
        title=title, slug=slugify(title), date_published=date,
        status=status, **kwargs)


class TestCategory(TestCase):
    def setUp(self):
        self.food_cat = create_category('Food')

    def test__str__(self):
        self.assertEquals(str(self.food_cat), 'Food')

    def test_get_absolute_url(self):
        self.assertEquals(
            self.food_cat.get_absolute_url(), '/en/categories/food/')


class TestTag(TestCase):
    def setUp(self):
        self.generic_tag = create_tag('Generic')

    def test__str__(self):
        self.assertEquals(str(self.generic_tag), 'Generic')


class TestPost(TestCase):
    def setUp(self):
        self.prev_post = create_post('Prev', datetime(2015, 3, 3))
        self.test_post = create_post('Test', datetime(2015, 4, 4))
        self.next_post = create_post('Next', datetime(2015, 5, 5))

    def test__str__(self):
        self.assertEquals(str(self.test_post), 'Test')

    def test_get_absolute_url(self):
        self.assertEquals(self.test_post.get_absolute_url(), '/en/test/')
        bs.POST_DETAIL_DATE_URL = True
        self.assertEquals(
            self.test_post.get_absolute_url(), '/en/2015/4/4/test/')
        bs.POST_DETAIL_DATE_URL = False

    def test_get_search_data(self):
        self.test_post.category = create_category('C', description='D')
        self.test_post.tags.add(create_tag('T'))
        add_plugin(self.test_post.body, 'TextPlugin', 'en', body='Hello')
        self.assertEquals(
            self.test_post.get_search_data(), 'Test Test C D T Hello')

    def test_get_meta_title(self):
        self.assertEquals(self.test_post.get_meta_title(), 'Test')
        self.test_post.meta_title = 'Test title'
        self.assertEquals(self.test_post.get_meta_title(), 'Test title')

    def test_get_meta_description(self):
        self.assertEquals(self.test_post.get_meta_description(), 'Test')
        self.test_post.meta_description = 'Test desc'
        self.assertEquals(self.test_post.get_meta_description(), 'Test desc')

    def test_name(self):
        self.assertEquals(self.test_post.name, 'Test')

    def test_is_published(self):
        self.test_post.status = Post.DRAFT
        self.assertEquals(self.test_post.is_published, False)
        self.test_post.status = Post.PUBLIC
        self.assertEquals(self.test_post.is_published, True)

    def test_previous_post(self):
        self.assertEquals(self.test_post.previous_post, self.prev_post)

    def test_next_post(self):
        self.assertEquals(self.test_post.next_post, self.next_post)

    def test_previous_next_posts(self):
        self.test_post.status = Post.PRIVATE
        self.assertEquals(self.test_post.previous_next_posts, (None, None))
        self.test_post.status = Post.PUBLIC
        setattr(self.test_post, 'previous_next', None)
        self.assertEquals(self.test_post.previous_next_posts,
                          (self.prev_post, self.next_post))
