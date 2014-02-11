# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import patterns, url

from blogit import settings as bs
from blogit.utils.translation import get_translation_regex
from blogit.views import (
    AuthorListView, AuthorDetailView, CategoryListView, CategoryDetailView,
    TagListView, TagDetailView, PostYearArchiveView, PostMonthArchiveView,
    PostDayArchiveView, PostListView, PostDetailView, PostDateDetailView)


# Post urls.
urlpatterns = patterns(
    '',
    # Post list.
    url(r'^$', PostListView.as_view(), name='blogit_post_list'),
)

if bs.POST_DETAIL_URL_BY_DATE:
    urlpatterns += patterns(
        '',
        # Post detail by date.
        url(r'^(?P<year>\d+)/(?P<month>[-\w\d]+)/(?P<day>\d+)'
            r'/(?P<slug>[-\w\d]+)/$', PostDateDetailView.as_view(),
            name='blogit_post_detail_by_date'),
    )
else:
    urlpatterns += patterns(
        '',
        # Post detail.
        url(r'^(?P<slug>[-\w\d]+)/$', PostDetailView.as_view(),
            name='blogit_post_detail'),
    )


# Archive urls.
if bs.ADD_ARCHIVE_URLS:
    urlpatterns = patterns(
        '',
        # Post archives list.
        url(r'^(?P<year>\d+)/(?P<month>[-\w\d]+)/(?P<day>\d+)/$',
            PostDayArchiveView.as_view(), name='blogit_post_archive_day'),

        url(r'^(?P<year>\d+)/(?P<month>[-\w\d]+)/$',
            PostMonthArchiveView.as_view(), name='blogit_post_archive_month'),

        url(r'^(?P<year>\d+)/$', PostYearArchiveView.as_view(),
            name='blogit_post_archive_year'),
    ) + urlpatterns


# Tag urls.
if bs.ADD_TAG_URLS:
    urlpatterns = patterns(
        '',
        # Tag list.
        url(r'^(?P<url>{})/$'.format(
            get_translation_regex(bs.TAG_URL, bs.TAG_URL_TRANSLATION)),
            TagListView.as_view(), name='blogit_tag_list'),

        # Tag detail.
        url(r'^(?P<url>{})/(?P<slug>[-\w]+)/$'.format(
            get_translation_regex(bs.TAG_URL, bs.TAG_URL_TRANSLATION)),
            TagDetailView.as_view(), name='blogit_tag_detail'),
    ) + urlpatterns


# Category urls.
if bs.ADD_CATEGORY_URLS:
    urlpatterns = patterns(
        '',
        # Category list.
        url(r'^(?P<url>{})/$'.format(
            get_translation_regex(
                bs.CATEGORY_URL, bs.CATEGORY_URL_TRANSLATION)),
            CategoryListView.as_view(), name='blogit_category_list'),

        # Category detail.
        url(r'^(?P<url>{})/(?P<slug>[-\w\d]+)/$'.format(
            get_translation_regex(
                bs.CATEGORY_URL, bs.CATEGORY_URL_TRANSLATION)),
            CategoryDetailView.as_view(), name='blogit_category_detail'),
    ) + urlpatterns


# Author urls.
if bs.ADD_AUTHOR_URLS:
    urlpatterns = patterns(
        '',
        # Author list.
        url(r'^(?P<url>{})/$'.format(
            get_translation_regex(
                bs.AUTHOR_URL, bs.AUTHOR_URL_TRANSLATION)),
            AuthorListView.as_view(), name='blogit_author_list'),

        # Author detail.
        url(r'^(?P<url>{})/(?P<slug>[-\w\d]+)/$'.format(
            get_translation_regex(bs.AUTHOR_URL, bs.AUTHOR_URL_TRANSLATION)),
            AuthorDetailView.as_view(), name='blogit_author_detail'),
    ) + urlpatterns
