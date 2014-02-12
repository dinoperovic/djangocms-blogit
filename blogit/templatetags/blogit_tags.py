# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template
from django.utils.six import string_types

from blogit.models import Post, Category


register = template.Library()


@register.assignment_tag
def get_posts(limit=None, category=None, author=None):
    # Returns posts by limit, category and author. 'category' and 'author'
    # can be passed in as string (slug) or as object.
    filters = {}

    # Add category to filters.
    if category:
        if isinstance(category, string_types):
            filters['category__translations__slug'] = category
        else:
            filters['category'] = category

    # Add author to filters.
    if author:
        if isinstance(author, string_types):
            filters['author__slug'] = author
        else:
            filters['author'] = author

    posts = Post.objects.public().filter(**filters)
    return posts.order_by('-date_published')[:limit]


@register.assignment_tag
def get_categories(limit=None):
    # Returns categories by limit.
    categories = Category.objects.all()
    return categories.order_by('-date_created')[:limit]
