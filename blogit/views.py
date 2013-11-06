# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect, HttpResponseForbidden, Http404
from django.shortcuts import render

from .models import Post

from blogit import utils


def list(request):
    """
    List of all posts.
    """
    posts = Post.objects.language().filter(is_public=True).order_by('-date_created')
    posts = utils.paginate(posts, request)

    return render(request, 'blogit/list.html', {'posts': posts})


def single(request, slug):
    """
    Sigle post.
    """
    try:
        post = Post.objects.language().get(slug=slug, is_public=True)
    except Post.DoesNotExist:
        raise Http404

    return render(request, 'blogit/single.html', {'post': post})