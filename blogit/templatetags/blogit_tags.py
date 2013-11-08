# -*- coding: utf-8 -*-
from django import template
from django.conf import settings as site_settings
from django.utils.translation import get_language

from blogit.models import Post, Category


register = template.Library()


@register.assignment_tag
def get_posts(limit, category=None, category_slug=None):
    """
    Returns posts.
    """

    posts = Post.objects.language().filter(is_public=True)

    # Filter posts by category if it exists.
    if category:
        try:
            cat = Category.objects.language().get(pk=category.pk)
            posts = posts.filter(categories=cat)
        except Category.DoesNotExist:
            category = None

    if category_slug and not category:
        for item in site_settings.LANGUAGES:
            try:
                cat = Category.objects.language(item[0]).get(slug=category_slug)
                posts = posts.filter(categories=cat)
                break
            except Category.DoesNotExist:
                category_slug = None

    return posts.order_by('-date_created')[:limit]


@register.assignment_tag
def get_categories():
    """
    Returns all categories.
    """
    categories = Category.objects.all()
    return categories.order_by('date_created')
