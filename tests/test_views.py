# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.test import TestCase

from blogit.models import Post

from .test_models import create_category, create_post, create_tag


class TestCategoryViews(TestCase):
    def setUp(self):
        self.game_cat = create_category('Game')
        self.food_cat = create_category('Food')
        self.inactive_cat = create_category('Inactive', active=False)
        self.test_post = create_post('Test', category=self.game_cat)

    def test_category_list(self):
        r = self.client.get(reverse('blogit_category_list'))
        self.assertEquals(r.status_code, 200)
        self.assertEquals(len(r.context[-1]['object_list']), 2)

    def test_category_detail(self):
        r = self.client.get(reverse('blogit_category_detail', args=['game']))
        self.assertEquals(r.status_code, 200)
        self.assertEquals(r.context[-1]['category'], self.game_cat)
        self.assertEquals(r.context[-1]['object_list'][0], self.test_post)


class TestTagViews(TestCase):
    def setUp(self):
        self.test_tag = create_tag('Test')
        self.test_tag2 = create_tag('Test2')
        self.test_tag3 = create_tag('Test3')
        self.test_post = create_post('Test')
        self.test_post.tags.add(self.test_tag)

    def test_tag_list(self):
        r = self.client.get(reverse('blogit_tag_list'))
        self.assertEquals(r.status_code, 200)
        self.assertEquals(len(r.context[-1]['object_list']), 3)

    def test_tag_detail(self):
        r = self.client.get(reverse('blogit_tag_detail', args=['test']))
        self.assertEquals(r.status_code, 200)
        self.assertEquals(r.context[-1]['tag'], self.test_tag)
        self.assertEquals(r.context[-1]['object_list'][0], self.test_post)


class TestPostViews(TestCase):
    def setUp(self):
        self.test_post = create_post('Test')
        self.public_post = create_post('Public')
        self.draft_post = create_post('Draft', status=Post.DRAFT)

    def test_post_list(self):
        r = self.client.get(reverse('blogit_post_list'))
        self.assertEquals(r.status_code, 200)
        self.assertEquals(len(r.context[-1]['object_list']), 2)

    def test_post_detail(self):
        r = self.client.get(reverse('blogit_post_detail', args=['test']))
        self.assertEquals(r.status_code, 200)
        self.assertEquals(r.context[-1]['object'], self.test_post)
