# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template
from django.utils.six import string_types

from blogit.models import Category, Post

register = template.Library()


@register.simple_tag(takes_context=True)
def get_posts(context, limit=None, category=None):
    request = context['request']
    filters = {}

    if category:
        if isinstance(category, string_types):
            filters['category__translations__slug'] = category
        else:
            filters['category'] = category

    return Post.objects.published(request, **filters)[:limit]


@register.simple_tag
def get_categories(limit=None):
    return Category.objects.filter(active=True)[:limit]
