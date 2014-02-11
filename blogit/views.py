# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.dates import (
    YearArchiveView, MonthArchiveView, DayArchiveView, DateDetailView)

from blogit import settings as bs
from blogit.utils.translation import check_translation_or_404
from blogit.models import Author, Category, Tag, Post


# Mixins
class PostListMixin(object):
    model = Post
    template_name = bs.POST_LIST_TEMPLATE
    context_object_name = 'posts'
    paginate_by = bs.POSTS_PER_PAGE
    filters = {}

    def get_queryset(self):
        qs = self.model.objects.public().filter(**self.filters)
        return qs.order_by('-date_published')


class PostDateMixin(object):
    date_field = 'date_published'
    month_format = bs.URL_MONTH_FORMAT
    year_format = bs.URL_YEAR_FORMAT
    day_format = bs.URL_DAY_FORMAT
    make_object_list = True
    allow_future = True


class PostDetailMixin(object):
    model = Post
    template_name = bs.POST_DETAIL_TEMPLATE
    context_object_name = 'post'


class ArchiveListMixin(PostDateMixin, PostListMixin):
    template_name = bs.ARCHIVE_LIST_TEMPLATE


# Author list.
class AuthorListView(ListView):
    model = Author
    template_name = bs.AUTHOR_LIST_TEMPLATE
    context_object_name = 'authors'
    paginate_by = bs.AUTHORS_PER_PAGE

    def get_queryset(self):
        return self.model.objects.language().all()

    def get(self, request, *args, **kwargs):
        check_translation_or_404(
            bs.AUTHOR_URL, bs.AUTHOR_URL_TRANSLATION, kwargs.get('url'))

        return super(AuthorListView, self).get(request, *args, **kwargs)


# Author detail.
class AuthorDetailView(DetailView):
    model = Author
    template_name = bs.AUTHOR_DETAIL_TEMPLATE
    context_object_name = 'author'

    def get_object(self):
        try:
            slug = self.kwargs.get('slug')
            return self.model.objects.language().get(slug=slug)
        except self.model.DoesNotExist:
            raise Http404()


# Category list.
class CategoryListView(ListView):
    model = Category
    template_name = bs.CATEGORY_LIST_TEMPLATE
    context_object_name = 'categories'
    paginate_by = bs.CATEGORIES_PER_PAGE

    def get_queryset(self):
        return self.model.objects.language().all()

    def get(self, request, *args, **kwargs):
        check_translation_or_404(
            bs.CATEGORY_URL, bs.CATEGORY_URL_TRANSLATION, kwargs.get('url'))

        return super(CategoryListView, self).get(request, *args, **kwargs)


# Category detail.
class CategoryDetailView(PostListMixin, ListView):
    template_name = bs.CATEGORY_DETAIL_TEMPLATE

    def get(self, request, *args, **kwargs):
        check_translation_or_404(
            bs.CATEGORY_URL, bs.CATEGORY_URL_TRANSLATION, kwargs.get('url'))

        # Add category filter to posts.
        try:
            category = Category.objects.language().get(slug=kwargs.get('slug'))
            self.filters = {'category': category}
        except Category.DoesNotExist:
            raise Http404()

        return super(CategoryDetailView, self).get(request, *args, **kwargs)


# Tag list.
class TagListView(ListView):
    model = Tag
    template_name = bs.TAG_LIST_TEMPLATE
    context_object_name = 'tags'
    paginate_by = bs.TAGS_PER_PAGE

    def get_queryset(self):
        return self.model.objects.all()

    def get(self, request, *args, **kwargs):
        check_translation_or_404(
            bs.TAG_URL, bs.TAG_URL_TRANSLATION, kwargs.get('url'))

        return super(TagListView, self).get(request, *args, **kwargs)


# Tag detail.
class TagDetailView(PostListMixin, ListView):
    template_name = bs.TAG_DETAIL_TEMPLATE

    def get(self, request, *args, **kwargs):
        check_translation_or_404(
            bs.TAG_URL, bs.TAG_URL_TRANSLATION, kwargs.get('url'))

        self.filters = {
            'tags__slug__iexact': kwargs.get('slug')
        }

        return super(TagDetailView, self).get(request, *args, **kwargs)


# Post archives list.
class PostYearArchiveView(ArchiveListMixin, YearArchiveView):
    pass


class PostMonthArchiveView(ArchiveListMixin, MonthArchiveView):
    pass


class PostDayArchiveView(ArchiveListMixin, DayArchiveView):
    pass


# Post list.
class PostListView(PostListMixin, ListView):
    pass


# Post detail.
class PostDetailView(PostDetailMixin, DetailView):
    def get_object(self):
        try:
            slug = self.kwargs.get('slug')
            return self.model.objects.public().get(slug=slug)
        except self.model.DoesNotExist:
            raise Http404()


class PostDateDetailView(PostDateMixin, PostDetailMixin, DateDetailView):
    def get_queryset(self):
        return self.model.objects.public().order_by('-date_published')
