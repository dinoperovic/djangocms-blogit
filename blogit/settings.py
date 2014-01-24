# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings


# Use AUTH_USER_MODEL as user.
AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


# How many posts per page are displayed.
AUTHORS_PER_PAGE = getattr(settings, 'BLOGIT_CATEGORIES_PER_PAGE', 5)
CATEGORIES_PER_PAGE = getattr(settings, 'BLOGIT_CATEGORIES_PER_PAGE', 5)
TAGS_PER_PAGE = getattr(settings, 'BLOGIT_TAGS_PER_PAGE', 5)
POSTS_PER_PAGE = getattr(settings, 'BLOGIT_POSTS_PER_PAGE', 5)


# Templates.
AUTHOR_LIST_TEMPLATE = getattr(
    settings, 'BLOGIT_AUTHOR_LIST_TEMPLATE', 'blogit/author/list.html')
AUTHOR_DETAIL_TEMPLATE = getattr(
    settings, 'BLOGIT_AUTHOR_LIST_TEMPLATE', 'blogit/author/detail.html')

CATEGORY_LIST_TEMPLATE = getattr(
    settings, 'BLOGIT_CATEGORY_LIST_TEMPLATE', 'blogit/category/list.html')
CATEGORY_DETAIL_TEMPLATE = getattr(
    settings, 'BLOGIT_CATEGORY_DETAIL_TEMPLATE', 'blogit/category/detail.html')

TAG_LIST_TEMPLATE = getattr(
    settings, 'BLOGIT_TAG_LIST_TEMPLATE', 'blogit/tag/list.html')
TAG_DETAIL_TEMPLATE = getattr(
    settings, 'BLOGIT_TAG_DETAIL_TEMPLATE', 'blogit/tag/detail.html')

POST_LIST_TEMPLATE = getattr(
    settings, 'BLOGIT_POST_LIST_TEMPLATE', 'blogit/list.html')
POST_DETAIL_TEMPLATE = getattr(
    settings, 'BLOGIT_POST_DETAIL_TEMPLATE', 'blogit/detail.html')

ARCHIVE_LIST_TEMPLATE = getattr(
    settings, 'BLOGIT_ARCHIVE_LIST_TEMPLATE', POST_LIST_TEMPLATE)


# Choices.
AUTHOR_LINK_TYPE_CHOICES = getattr(
    settings, 'BLOGIT_AUTHOR_LINK_TYPE_CHOICES', ())


# Url defaults and translations.
AUTHOR_URL = getattr(settings, 'BLOGIT_AUTHOR_URL', 'authors')
AUTHOR_URL_TRANSLATION = getattr(
    settings, 'BLOGIT_AUTHOR_URL_TRANSLATION', ())

CATEGORY_URL = getattr(settings, 'BLOGIT_CATEGORY_URL', 'categories')
CATEGORY_URL_TRANSLATION = getattr(
    settings, 'BLOGIT_CATEGORY_URL_TRANSLATION', ())

TAG_URL = getattr(settings, 'BLOGIT_TAG_URL', 'tags')
TAG_URL_TRANSLATION = getattr(
    settings, 'BLOGIT_TAG_URL_TRANSLATION', ())


# Show detail url by date.
POST_DETAIL_URL_BY_DATE = getattr(
    settings, 'BLOGIT_POST_DETAIL_URL_BY_DATE', False)


# Url date formats.
URL_YEAR_FORMAT = getattr(settings, 'BLOGIT_URL_YEAR_FORMAT', '%Y')
URL_MONTH_FORMAT = getattr(settings, 'BLOGIT_URL_MONTH_FORMAT', '%m')
URL_DAY_FORMAT = getattr(settings, 'BLOGIT_URL_DAY_FORMAT', '%d')
