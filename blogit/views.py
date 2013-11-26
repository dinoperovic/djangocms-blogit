# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect, HttpResponseForbidden, Http404
from django.shortcuts import render
from django.utils.translation import get_language

from blogit.models import Post, Category, Author
from blogit import settings, utils


def post_list(request, posts=None, extra_context=None):
    """
    List posts.
    """
    posts = posts if posts else Post.objects.all()
    posts = utils.paginate(posts.filter(is_public=True).order_by('-date_created'), request)

    context = {'posts': posts}
    if extra_context:
        context.update(extra_context)

    return render(request, 'blogit/list.html', context)


def category_list(request, category_url, category_slug):
    """
    List posts with given category.
    """

    # Raise 404 if current language doesn't match category_url.
    if settings.BLOGIT_CATEGORY_URL_TRANSLATIONS:
        if utils.get_translation('category', settings.BLOGIT_CATEGORY_URL_TRANSLATIONS) != category_url:
            raise Http404

    try:
        category = Category.objects.language().get(slug=category_slug)
        return post_list(request, Post.objects.language().filter(categories=category), {'category': category})
    except Category.DoesNotExist:
        raise Http404


def author_list(request, author_url, author_slug):
    """
    List posts with given author.
    """

    # Raise 404 if current language doesn't match author_url.
    if settings.BLOGIT_AUTHOR_URL_TRANSLATIONS:
        if utils.get_translation('author', settings.BLOGIT_AUTHOR_URL_TRANSLATIONS) != author_url:
            raise Http404

    try:
        author = Author.objects.language().get(slug=author_slug)
        return post_list(request, Post.objects.language().filter(author=author), {'author': author})
    except Author.DoesNotExist:
        raise Http404


def single(request, post_slug):
    """
    Sigle post.
    """
    try:
        post = Post.objects.language().get(slug=post_slug, is_public=True)
    except Post.DoesNotExist:
        raise Http404

    return render(request, 'blogit/single.html', {'post': post})
