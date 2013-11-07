# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect, HttpResponseForbidden, Http404
from django.shortcuts import render

from .models import Post, Category

from blogit import utils


def list(request, category_slug=None):
    """
    List of all posts.
    """
    posts = Post.objects.language().filter(is_public=True)

    if category_slug:
        category_id = Category.objects.language().get(slug=category_slug)
        posts = posts.filter(categories=category_id)

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