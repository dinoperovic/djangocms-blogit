# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template
from django.utils.six import string_types

from blogit.models import Post, Category


register = template.Library()


@register.assignment_tag
def get_posts(limit=None, category=None):
    filters = {}

    if category:
        if isinstance(category, string_types):
            filters['category__translations__slug'] = category
        else:
            filters['category'] = category

    return Post.objects.language().published(**filters)[:limit]


@register.assignment_tag
def get_categories(limit=None):
    return Category.objects.language().filter(active=True)[:limit]
