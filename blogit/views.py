# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect, HttpResponseForbidden, Http404
from django.shortcuts import render
from django.utils.translation import get_language

from .models import Post, Category

from blogit import settings, utils


def list(request, category_url=None, category_slug=None):
    """
    List of all posts.
    """

    # Raise 404 if current language doesn't match category_url.
    if category_url and settings.BLOGIT_CATEGORY_URL_TRANSLATIONS:
        if utils.get_translation(None, settings.BLOGIT_CATEGORY_URL_TRANSLATIONS) != category_url:
            raise Http404

    posts = Post.objects.language().filter(is_public=True)

    if category_slug:
        try:
            category_id = Category.objects.language().get(slug=category_slug)
            posts = posts.filter(categories=category_id)
        except Category.DoesNotExist:
            raise Http404

    posts = utils.paginate(posts.order_by('-date_created'), request)

    return render(request, 'blogit/list.html', {'posts': posts})


def single(request, post_slug):
    """
    Sigle post.
    """
    try:
        post = Post.objects.language().get(slug=post_slug, is_public=True)
    except Post.DoesNotExist:
        raise Http404

    return render(request, 'blogit/single.html', {'post': post})