# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from . import settings as bs
from .utils.translation import get_translation_regex
from .views import (
    PostListView, PostDetailView, PostYearArchiveView, PostMonthArchiveView,
    PostDayArchiveView, PostDateDetailView, CategoryListView, AuthorListView,
    AuthorDetailView)


urlpatterns = patterns(
    '',
    # Category detail.
    url(r'^(?P<url>{})/(?P<slug>[-\w\d]+)/$'.format(
        get_translation_regex(bs.CATEGORY_URL, bs.CATEGORY_URL_TRANSLATION)),
        CategoryListView.as_view(), name='blogit_category_detail'),

    # Category list.
    url(r'^(?P<url>{})/$'.format(
        get_translation_regex(bs.CATEGORY_URL, bs.CATEGORY_URL_TRANSLATION)),
        CategoryListView.as_view(), name='blogit_category_list'),

    # Author detail.
    url(r'^(?P<url>{})/(?P<slug>[-\w\d]+)/$'.format(
        get_translation_regex(bs.AUTHOR_URL, bs.AUTHOR_URL_TRANSLATION)),
        AuthorDetailView.as_view(), name='blogit_author_detail'),

    # Author list.
    url(r'^(?P<url>{})/$'.format(
        get_translation_regex(
            bs.AUTHOR_URL, bs.AUTHOR_URL_TRANSLATION)),
        AuthorListView.as_view(), name='blogit_author_list'),

    # Post archives.
    url(r'^(?P<year>\d+)/(?P<month>[-\w\d]+)/(?P<day>\d+)/$',
        PostDayArchiveView.as_view(), name='blogit_post_archive_day'),

    url(r'^(?P<year>\d+)/(?P<month>[-\w\d]+)/$',
        PostMonthArchiveView.as_view(), name='blogit_post_archive_month'),

    url(r'^(?P<year>\d+)/$', PostYearArchiveView.as_view(),
        name='blogit_post_archive_year'),

    # Post list.
    url(r'^$', PostListView.as_view(), name='blogit_post_list'),
)

# Add detail patterns.
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
