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
    slug_regexp = r'(?P<slug>[-_\w\d]+)'
    path_regexp = r'(?P<path>[-_/\w\d]+)'
    list_regexp = r'^$'
    detail_regexp = r'^%s/$' % slug_regexp

    if name == 'archive':
        return [
            url(r'^(?P<year>\d+)/(?P<month>[-\w\d]+)/(?P<day>\d+)/$', PostDayArchiveView.as_view(),
                name='blogit_post_archive_day'),
            url(r'^(?P<year>\d+)/(?P<month>[-\w\d]+)/$', PostMonthArchiveView.as_view(),
                name='blogit_post_archive_month'),
            url(r'^(?P<year>\d+)/$', PostYearArchiveView.as_view(), name='blogit_post_archive_year'),
        ]

    elif name == 'categories':
        detail_regexp = r'^%s/$' % path_regexp

        if bs.SINGLE_APPHOOK:
            list_regexp = _(r'^categories/$')
            detail_regexp = _(r'^categories/%s/$') % path_regexp

        return [
            url(list_regexp, CategoryListView.as_view(), name='blogit_category_list'),
            url(detail_regexp, CategoryDetailView.as_view(), name='blogit_category_detail'),
        ]

    elif name == 'tags':
        if bs.SINGLE_APPHOOK:
            list_regexp = _(r'^tags/$')
            detail_regexp = _(r'^tags/%s/$') % slug_regexp

        return [
            url(list_regexp, TagListView.as_view(), name='blogit_tag_list'),
            url(detail_regexp, TagDetailView.as_view(), name='blogit_tag_detail'),
        ]

    elif name == 'feeds':
        regex_rss = r'rss/$'
        regex_rss_tag = r'^rss/%s/$' % slug_regexp
        regex_atom = r'atom/$'
        regex_atom_tag = r'^atom/%s/$' % slug_regexp

        if bs.SINGLE_APPHOOK:
            list_regexp = _(r'feeds/$')
            regex_rss = _(r'feeds/rss/$')
            regex_rss_tag = _(r'feeds/^rss/%s/$') % slug_regexp
            regex_atom = _(r'feeds/atom/$')
            regex_atom_tag = _(r'feeds/^atom/%s/$') % slug_regexp

        default_name = 'blogit_%s_feed' % bs.FEED_DEFAULT

        return [
            url(list_regexp, RedirectView.as_view(pattern_name=default_name), name='blogit_feed'),
            url(regex_rss, PostRssFeed(), name='blogit_rss_feed'),
            url(regex_rss_tag, PostRssFeed(), name='blogit_rss_feed_tag'),
            url(regex_atom, PostAtomFeed(), name='blogit_atom_feed'),
            url(regex_atom_tag, PostAtomFeed(), name='blogit_atom_feed_tag'),
        ]

    elif name == 'posts':
        return [
            url(list_regexp, PostListView.as_view(), name='blogit_post_list'),
            url(r'^(?P<year>\d+)/(?P<month>[-\w\d]+)/(?P<day>\d+)/%s/$' % slug_regexp, PostDateDetailView.as_view(),
                name='blogit_post_detail_date'),
            url(detail_regexp, PostDetailView.as_view(), name='blogit_post_detail'),
        ]


urlpatterns = []
for module in ('archive', 'categories', 'tags', 'feeds', 'posts'):
    urlpatterns.extend(get_urls(module))
