# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.utils.translation import activate

from blogit.models import Author


class AuthorTestCase(TestCase):
    fixtures = [
        'blogit_author_testdata.json',
        'blogit_post_testdata.json',
    ]

    def setUp(self):
        self.john = Author.objects.get(pk=1)
        self.jane = Author.objects.get(pk=2)
        self.mark = Author.objects.get(pk=3)

    def test__str__(self):
        self.assertEqual(self.john.__str__(), 'John')

    def test_get_absolute_url(self):
        activate('en')
        self.assertEqual(self.john.get_absolute_url(), '/en/authors/john-doe/')
        activate('it')
        self.assertEqual(self.jane.get_absolute_url(), '/it/autori/jane-roe/')
        activate('hr')
        self.assertEqual(self.mark.get_absolute_url(), '/hr/autori/mark-moe/')

    def test_get_slug(self):
        self.assertEqual(self.john.get_slug(), 'john-doe')

    def test_get_first_name(self):
        self.assertEqual(self.john.get_first_name(), 'John')
        self.assertEqual(self.jane.get_first_name(), 'Jane')
        self.assertEqual(self.mark.get_first_name(), 'Mark')

    def test_get_last_name(self):
        self.assertFalse(self.john.get_last_name())
        self.assertEqual(self.jane.get_last_name(), 'Overriden Roe')
        self.assertEqual(self.mark.get_last_name(), 'Moe')

    def test_get_full_name(self):
        self.assertEqual(self.john.get_full_name(), 'John')
        self.assertEqual(self.jane.get_full_name(), 'Jane Overriden Roe')
        self.assertEqual(self.mark.get_full_name(), 'Mark Moe')

    def test_get_email(self):
        self.assertEqual(self.john.get_email(), 'john.doe@example.com')
        self.assertEqual(self.jane.get_email(), 'jane.roe@example.com')
        self.assertFalse(self.mark.get_email())

    def test_get_posts(self):
        self.assertEqual(self.john.get_posts().count(), 2)
        self.assertEqual(self.jane.get_posts().count(), 1)
        self.assertFalse(self.mark.get_posts().count())


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
