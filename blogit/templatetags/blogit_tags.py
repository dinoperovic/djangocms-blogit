# -*- coding: utf-8 -*-
from django import template

from blogit.models import Post, Category


register = template.Library()


@register.assignment_tag
def get_posts(limit):
    # Returns posts by limit.
    posts = Post.objects.language().filter(is_public=True)
    return posts[:limit]


@register.assignment_tag
def get_categories():
    # Returns all categories.
    categories = Category.objects.all()
    return categories.order_by('date_created')
