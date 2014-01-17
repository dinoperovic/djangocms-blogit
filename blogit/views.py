# -*- coding: utf-8 -*-
from django.http import Http404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.dates import (
    YearArchiveView, MonthArchiveView, DayArchiveView, DateDetailView)

from . import settings as bs
from .utils.translation import check_translation_or_404
from .models import Post, Category, Author


class PostListMixin(object):
    model = Post
    template_name = bs.POST_LIST_TEMPLATE
    context_object_name = 'posts'
    paginate_by = bs.POSTS_PER_PAGE
    filters = {}

    def get_queryset(self):
        return self.model.objects.language().filter(
            is_public=True, **self.filters).order_by('-date_published')


class PostDateMixin(object):
    date_field = ('date_published')
    month_format = bs.URL_MONTH_FORMAT
    year_format = bs.URL_YEAR_FORMAT
    day_format = bs.URL_DAY_FORMAT
    make_object_list = True
    allow_future = True


class ArchiveListMixin(PostDateMixin, PostListMixin):
    template_name = bs.ARCHIVE_LIST_TEMPLATE


class PostListView(PostListMixin, ListView):
    pass


class CategoryListView(PostListMixin, ListView):
    def get(self, request, *args, **kwargs):
        check_translation_or_404(
            bs.CATEGORY_URL, bs.CATEGORY_URL_TRANSLATION, kwargs.get('url'))

        # Add category filter to posts.
        try:
            category = Category.objects.language().get(
                slug=kwargs.get('slug'))
            self.filters = {'category': category}
        except Category.DoesNotExist:
            raise Http404()

        return super(CategoryListView, self).get(request, *args, **kwargs)


class PostYearArchiveView(ArchiveListMixin, YearArchiveView):
    pass


class PostMonthArchiveView(ArchiveListMixin, MonthArchiveView):
    pass


class PostDayArchiveView(ArchiveListMixin, DayArchiveView):
    pass


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


class AuthorDetailView(DetailView):
    model = Author
    template_name = bs.AUTHOR_DETAIL_TEMPLATE
    context_object_name = 'author'

    def get_object(self):
        try:
            return self.model.objects.language().get(
                slug=self.kwargs.get('slug'))
        except self.model.DoesNotExist:
            try:
                return self.model.objects.language().get(
                    pk=self.kwargs.get('slug'))
            except self.model.DoesNotExist:
                raise Http404()


class PostDetailMixin(object):
    model = Post
    template_name = bs.POST_DETAIL_TEMPLATE
    context_object_name = 'post'


class PostDetailView(PostDetailMixin, DetailView):
    def get_object(self):
        try:
            return self.model.objects.language().get(
                slug=self.kwargs.get('slug'), is_public=True)
        except self.model.DoesNotExist:
            raise Http404()


class PostDateDetailView(PostDateMixin, PostDetailMixin, DateDetailView):
    def get_queryset(self):
        return self.model.objects.language().filter(
            is_public=True).order_by('-date_published')
