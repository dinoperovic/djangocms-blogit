# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.http import Http404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.dates import (
    YearArchiveView, MonthArchiveView, DayArchiveView, DateDetailView)
from django.utils.translation import ugettext_lazy as _

from blogit import settings as bs
from blogit.models import Category, Post


class ToolbarMixin(object):
    def get(self, request, *args, **kwargs):
        response = super(ToolbarMixin, self).get(request, *args, **kwargs)

        if hasattr(self, 'object') and hasattr(request, 'toolbar'):
            request.toolbar.set_object(self.object)
            menu = request.toolbar.get_menu('blogit-current-menu')
            if menu:
                self.update_menu(menu, self.object)

        return response

    def update_menu(self, menu, obj):
        pass


class PostListMixin(object):
    model = Post
    template_name = 'blogit/post_list.html'
    paginate_by = bs.POSTS_PER_PAGE
    filters = {'active': True}

    def get_queryset(self):
        return Post.objects.translated().published(**self.filters)


# Category views.
class CategoryListView(ListView):
    model = Category
    template_name = 'blogit/category_list.html'

    def get_queryset(self):
        return self.model.objects.translated().filter(active=True)


class CategoryDetailView(ToolbarMixin, PostListMixin, ListView):
    template_name = 'blogit/category_detail.html'

    def get_context_data(self, **kwargs):
        kwargs.update({'category': self.object})
        return super(CategoryDetailView, self).get_context_data(**kwargs)

    def get(self, request, *args, **kwargs):
        try:
            self.object = Category.objects.translated().get(
                active=True, translations__slug=kwargs.get('slug'))
            self.filters = {'category_id': self.object.pk}
        except Category.DoesNotExist:
            raise Http404

        return super(CategoryDetailView, self).get(request, *args, **kwargs)

    def update_menu(self, menu, obj):
        menu.add_break()
        url = reverse(
            'admin:blogit_category_change', args=[self.object.pk])
        menu.add_modal_item(_('Edit this Category'), url=url)
        menu.add_break()
        url = reverse(
            'admin:blogit_category_delete', args=[self.object.pk])
        menu.add_modal_item(_('Delete Category'), url=url)


class PostDateMixin(object):
    date_field = 'date_published'
    year_format = '%Y'
    month_format = '%m'
    day_format = '%d'
    make_object_list = True
    allow_future = True


class ArchiveListMixin(PostDateMixin, PostListMixin):
    template_name = 'blogit/post_list.html'


class PostYearArchiveView(ArchiveListMixin, YearArchiveView):
    pass


class PostMonthArchiveView(ArchiveListMixin, MonthArchiveView):
    pass


class PostDayArchiveView(ArchiveListMixin, DayArchiveView):
    pass


class PostListView(PostListMixin, ListView):
    pass


class PostDetailMixin(ToolbarMixin):
    model = Post
    template_name = 'blogit/post_detail.html'
    slug_field = 'translations__slug'

    def get_queryset(self):
        return Post.objects.translated().published()

    def update_menu(self, menu, obj):
        menu.add_break()
        url = reverse(
            'admin:blogit_post_change', args=[self.object.pk])
        menu.add_modal_item(_('Edit this Post'), url=url)
        menu.add_break()

        url = reverse(
            'admin:blogit_post_delete', args=[self.object.pk])
        menu.add_modal_item(_('Delete Post'), url=url)


class PostDetailView(PostDetailMixin, DetailView):
    pass


class PostDateDetailView(PostDateMixin, PostDetailMixin, DateDetailView):
    pass
