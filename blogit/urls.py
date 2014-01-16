# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from . import settings as bs
from .utils import get_translation_regex
from .views import (
    PostListView, PostDetailView,
    CategoryListView,
    AuthorListView, AuthorDetailView)


urlpatterns = patterns(
    '',
    # Category list.
    url(r'^(?P<url>{})/(?P<slug>[-\w\d]+)/$'.format(
        get_translation_regex(bs.CATEGORY_URL, bs.CATEGORY_URL_TRANSLATION)),
        CategoryListView.as_view(), name='blogit_category'),

    # Author detail.
    url(r'^(?P<url>{})/(?P<slug>[-\w\d]+)/$'.format(
        get_translation_regex(bs.AUTHOR_URL, bs.AUTHOR_URL_TRANSLATION)),
        AuthorDetailView.as_view(), name='blogit_author_detail'),

    # Author list.
    url(r'^(?P<url>{})/$'.format(
        get_translation_regex(
            bs.AUTHOR_URL, bs.AUTHOR_URL_TRANSLATION)),
        AuthorListView.as_view(), name='blogit_author_list'),

    # Post detail.
    url(r'^(?P<slug>[-\w\d]+)/$', PostDetailView.as_view(),
        name='blogit_post_detail'),

    # Post list.
    url(r'^$', PostListView.as_view(), name='blogit_post_list'),
)
