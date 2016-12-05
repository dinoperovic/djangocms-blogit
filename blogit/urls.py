# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _
from django.views.generic import RedirectView

from blogit import settings as bs
from blogit.feeds import PostAtomFeed, PostRssFeed
from blogit.views import (CategoryDetailView, CategoryListView, PostDateDetailView, PostDayArchiveView, PostDetailView,
                          PostListView, PostMonthArchiveView, PostYearArchiveView, TagDetailView, TagListView)


def get_urls(name):
    """
    Returns url patterns for the given module.
    Checks if urls are handled with single or multiple apphooks.
    """
    regex_list = r'^$'
    regex_detail = r'^(?P<slug>[-\w\d]+)/$'

    if name == 'archive':
        return [
            url(r'^(?P<year>\d+)/(?P<month>[-\w\d]+)/(?P<day>\d+)/$',
                PostDayArchiveView.as_view(), name='blogit_post_archive_day'),
            url(r'^(?P<year>\d+)/(?P<month>[-\w\d]+)/$',
                PostMonthArchiveView.as_view(),
                name='blogit_post_archive_month'),
            url(r'^(?P<year>\d+)/$', PostYearArchiveView.as_view(),
                name='blogit_post_archive_year'),
        ]

    elif name == 'categories':
        if bs.SINGLE_APPHOOK:
            regex_list = _(r'^categories/$')
            regex_detail = _(r'^categories/(?P<slug>[-\w\d]+)/$')

        return [
            url(regex_list, CategoryListView.as_view(),
                name='blogit_category_list'),
            url(regex_detail, CategoryDetailView.as_view(),
                name='blogit_category_detail'),
        ]

    elif name == 'tags':
        if bs.SINGLE_APPHOOK:
            regex_list = _(r'^tags/$')
            regex_detail = _(r'^tags/(?P<slug>[-\w\d]+)/$')

        return [
            url(regex_list, TagListView.as_view(), name='blogit_tag_list'),
            url(regex_detail, TagDetailView.as_view(),
                name='blogit_tag_detail'),
        ]

    elif name == 'feeds':
        regex_rss = r'rss/$'
        regex_rss_tag = r'^rss/(?P<tag_slug>[-\w\d]+)/$'
        regex_atom = r'atom/$'
        regex_atom_tag = r'^atom/(?P<tag_slug>[-\w\d]+)/$'

        if bs.SINGLE_APPHOOK:
            regex_list = _(r'feeds/$')
            regex_rss = _(r'feeds/rss/$')
            regex_rss_tag = _(r'feeds/^rss/(?P<tag_slug>[-\w\d]+)/$')
            regex_atom = _(r'feeds/atom/$')
            regex_atom_tag = _(r'feeds/^atom/(?P<tag_slug>[-\w\d]+)/$')

        default_name = 'blogit_%s_feed' % bs.FEED_DEFAULT

        return [
            url(regex_list, RedirectView.as_view(pattern_name=default_name),
                name='blogit_feed'),
            url(regex_rss, PostRssFeed(), name='blogit_rss_feed'),
            url(regex_rss_tag, PostRssFeed(), name='blogit_rss_feed_tag'),
            url(regex_atom, PostAtomFeed(), name='blogit_atom_feed'),
            url(regex_atom_tag, PostAtomFeed(), name='blogit_atom_feed_tag'),
        ]

    elif name == 'posts':
        return [
            url(regex_list, PostListView.as_view(), name='blogit_post_list'),
            url(r'^(?P<year>\d+)/(?P<month>[-\w\d]+)/(?P<day>\d+)'
                r'/(?P<slug>[-\w\d]+)/$', PostDateDetailView.as_view(),
                name='blogit_post_detail_date'),
            url(regex_detail, PostDetailView.as_view(),
                name='blogit_post_detail'),
        ]


urlpatterns = []
for module in ('archive', 'categories', 'tags', 'feeds', 'posts'):
    urlpatterns.extend(get_urls(module))
