# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys

from django.contrib.auth.models import User
from django.test import TestCase
from django.utils.text import slugify

from blogit.models import Author, Post


class AuthorTestCase(TestCase):
    fixtures = ['blogit_testdata.json']

    def setUp(self):
        jane_user = User.objects.create(
            username='janedoe',
            password='pass',
            last_name='Doe',
            first_name='Jane',
            email='jane.doe@example.com')

        self.john = Author.objects.create(
            first_name='John',
            slug='john-doe',
            email='john.doe@example.com')

        self.jane = Author.objects.create(
            user=jane_user,
            last_name='Overriden Doe')

        test_post = Post.objects.all()
        sys.stderr.write('%s' % test_post.__str__())

        for i in range(5):
            title = 'Post #{}'.format(i)
            Post.objects.create(
                title=title, slug=slugify(title), author=self.john)

    def test__str__(self):
        pass

    def test_get_absolute_url(self):
        self.assertEqual(self.john.get_absolute_url(), '/authors/john-doe/')

    def test_get_slug(self):
        self.assertEqual(self.john.get_slug(), 'john-doe')
        self.assertEqual(self.jane.get_slug(), self.jane.pk)

    def test_get_first_name(self):
        self.assertEqual(self.john.get_first_name(), 'John')
        self.assertEqual(self.jane.get_first_name(), 'Jane')

    def test_get_last_name(self):
        self.assertFalse(self.john.get_last_name())
        self.assertEqual(self.jane.get_last_name(), 'Overriden Doe')

    def test_get_full_name(self):
        self.assertEqual(self.john.get_full_name(), 'John')
        self.assertEqual(self.jane.get_full_name(), 'Jane Overriden Doe')

    def test_get_email(self):
        self.assertEqual(self.john.get_email(), 'john.doe@example.com')
        self.assertEqual(self.jane.get_email(), 'jane.doe@example.com')

    def test_get_posts(self):
        posts = self.john.get_posts()
        self.assertEqual(posts.count(), 5)


class CategoryTestCase(TestCase):
    def setUp(self):
        pass

    def test__str__(self):
        pass

    def test_save(self):
        pass

    def test_get_absolute_url(self):
        pass

    def test_get_slug(self):
        pass


class TagTestCase(TestCase):
    def setUp(self):
        pass

    def test__str__(self):
        pass

    def test_get_absolute_url(self):
        pass


class TaggedPostTestCase(TestCase):
    def setUp(self):
        pass

    def test__str__(self):
        pass

    def test_tags_for(self):
        pass


class PostTestCase(TestCase):
    def setUp(self):
        pass

    def test__str__(self):
        pass

    def test_save(self):
        pass

    def test_get_absolute_url(self):
        pass

    def test_get_slug(self):
        pass

    def get_tags(self):
        pass

    def test_get_previous(self):
        pass

    def test_get_next(self):
        pass
