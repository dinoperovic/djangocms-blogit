# -*- coding: utf-8 -*-
from django.http import Http404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from . import settings as bs
from .utils import get_translation
from .models import Post, Category, Author


class PostListMixin(object):
    model = Post
    template_name = bs.LIST_TEMPLATE
    context_object_name = 'posts'
    paginate_by = bs.POSTS_PER_PAGE
    filters = {}

    def get_queryset(self):
        return super(PostListMixin, self).get_queryset().filter(
            translations__is_public=True, **self.filters)

    def check_url_translation(self, default, translation, url):
        # Raise 404 if translation doesn't match the url.
        if get_translation(default, translation) != url:
            raise Http404


class PostListView(PostListMixin, ListView):
    pass


class CategoryListView(PostListMixin, ListView):
    def get(self, request, *args, **kwargs):
        self.check_url_translation(
            bs.CATEGORY_URL, bs.CATEGORY_URL_TRANSLATION, kwargs.get('url'))

        # Add category filter to posts.
        try:
            category = Category.objects.language().get(
                slug=kwargs.get('slug'))
            self.filters.update({'category': category})
        except Category.DoesNotExist:
            raise Http404

        return super(CategoryListView, self).get(request, *args, **kwargs)


class AuthorListView(PostListMixin, ListView):
    def get(self, request, *args, **kwargs):
        self.check_url_translation(
            bs.AUTHOR_URL, bs.AUTHOR_URL_TRANSLATION, kwargs.get('url'))

        # Add author filter to posts.
        try:
            author = Author.objects.language().get(slug=kwargs.get('slug'))
            self.filters.update({'author': author})
        except Author.DoesNotExist:
            raise Http404

        return super(AuthorListView, self).get(request, *args, **kwargs)


class PostDetailView(DetailView):
    model = Post
    template_name = bs.DETAIL_TEMPLATE
    context_object_name = 'post'

    def get_object(self):
        try:
            return Post.objects.language().get(
                slug=self.kwargs.get('slug'), is_public=True)
        except Post.DoesNotExist:
            raise Http404
