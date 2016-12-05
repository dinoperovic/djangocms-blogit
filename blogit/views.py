# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.http import Http404
from django.utils.translation import ugettext_lazy as _
from django.views.generic.dates import DateDetailView, DayArchiveView, MonthArchiveView, YearArchiveView
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from parler.views import TranslatableSlugMixin, ViewUrlMixin

from blogit import settings as bs
from blogit.models import Category, Post, Tag


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

    def __init__(self, *args, **kwargs):
        super(PostListMixin, self).__init__(*args, **kwargs)
        self.filters = {}

    def get_queryset(self):
        return self.model.objects.published(self.request, **self.filters)


# Category views.
class CategoryListView(ListView):
    model = Category
    template_name = 'blogit/category_list.html'

    def get_queryset(self):
        return self.model.objects.filter(active=True)


class CategoryDetailView(ToolbarMixin, ViewUrlMixin, PostListMixin, ListView):
    template_name = 'blogit/category_detail.html'

    def get_context_data(self, **kwargs):
        kwargs.update({'category': self.get_category_object()})
        return super(CategoryDetailView, self).get_context_data(**kwargs)

    def get(self, request, *args, **kwargs):
        try:
            ids = self.get_category_object().get_descendants(include_self=True).values_list('id', flat=True)
            self.filters['category_id__in'] = ids
        except Category.DoesNotExist:
            raise Http404
        return super(CategoryDetailView, self).get(request, *args, **kwargs)

    def get_category_object(self):
        if not hasattr(self, '_category_object'):
            path = self.kwargs['path']
            slug = path.split('/').pop()
            queryset = Category.objects.translated(slug=slug)
            category = get_object_or_404(queryset, active=True)
            if category.get_path() != path:
                raise Http404
            setattr(self, '_category_object', category)
        return getattr(self, '_category_object')

    def update_menu(self, menu, obj):
        pk = self.get_category_object().id
        menu.add_break()
        url = reverse('admin:blogit_category_change', args=[pk])
        menu.add_modal_item(_('Edit Category'), url=url)
        url = reverse('admin:blogit_category_delete', args=[pk])
        menu.add_modal_item(_('Delete Category'), url=url)

    def get_view_url(self):
        """
        Return object view url. Used in `get_translated_url` templatetag from parler.
        """
        return self.get_category_object().get_absolute_url()


# Tag views.
class TagListView(ListView):
    model = Tag
    template_name = 'blogit/tag_list.html'

    def get_queryset(self):
        return self.model.objects.filter(active=True)


class TagDetailView(ToolbarMixin, PostListMixin, ListView):
    template_name = 'blogit/tag_detail.html'

    def get_context_data(self, **kwargs):
        kwargs.update({'tag': self.object})
        return super(TagDetailView, self).get_context_data(**kwargs)

    def get(self, request, *args, **kwargs):
        try:
            self.object = Tag.objects.translated(slug=kwargs.get('slug')).get(active=True)
            self.filters['tags__in'] = [self.object]
        except Tag.DoesNotExist:
            raise Http404

        return super(TagDetailView, self).get(request, *args, **kwargs)

    def update_menu(self, menu, obj):
        menu.add_break()
        url = reverse('admin:blogit_tag_change', args=[self.object.pk])
        menu.add_modal_item(_('Edit Tag'), url=url)
        url = reverse('admin:blogit_tag_delete', args=[self.object.pk])
        menu.add_modal_item(_('Delete Tag'), url=url)


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

    def get_queryset(self):
        return Post.objects.published(self.request)

    def update_menu(self, menu, obj):
        menu.add_break()
        url = reverse('admin:blogit_post_change', args=[self.object.pk])
        menu.add_modal_item(_('Edit Post'), url=url)

        url = reverse('admin:blogit_post_delete', args=[self.object.pk])
        menu.add_modal_item(_('Delete Post'), url=url)


class PostDetailView(PostDetailMixin, TranslatableSlugMixin, DetailView):
    pass


class PostDateDetailView(PostDateMixin, PostDetailMixin, DateDetailView):
    pass
