# -*- coding: utf-8 -*-
from django.conf import settings


# Use AUTH_USER_MODEL as user.
AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

# How many posts per page are displayed.
POSTS_PER_PAGE = getattr(settings, 'BLOGIT_POSTS_PER_PAGE', 5)
AUTHORS_PER_PAGE = getattr(settings, 'BLOGIT_AUTHORS_PER_PAGE', 5)

# Templates.
POST_LIST_TEMPLATE = getattr(
    settings, 'BLOGIT_POST_LIST_TEMPLATE', 'blogit/list.html')
POST_DETAIL_TEMPLATE = getattr(
    settings, 'BLOGIT_POST_DETAIL_TEMPLATE', 'blogit/detail.html')

ARCHIVE_LIST_TEMPLATE = getattr(
    settings, 'BLOGIT_ARCHIVE_LIST_TEMPLATE', POST_LIST_TEMPLATE)

AUTHOR_LIST_TEMPLATE = getattr(
    settings, 'BLOGIT_AUTHOR_LIST_TEMPLATE', 'blogit/author/list.html')
AUTHOR_DETAIL_TEMPLATE = getattr(
    settings, 'BLOGIT_AUTHOR_LIST_TEMPLATE', 'blogit/author/detail.html')

# Choices.
AUTHOR_LINK_TYPE_CHOICES = getattr(
    settings, 'BLOGIT_AUTHOR_LINK_TYPE_CHOICES', ())

# Url defaults and translations.
CATEGORY_URL = getattr(settings, 'BLOGIT_CATEGORY_URL', 'categories')
CATEGORY_URL_TRANSLATION = getattr(
    settings, 'BLOGIT_CATEGORY_URL_TRANSLATION', ())

AUTHOR_URL = getattr(settings, 'BLOGIT_AUTHOR_URL', 'authors')
AUTHOR_URL_TRANSLATION = getattr(
    settings, 'BLOGIT_AUTHOR_URL_TRANSLATION', ())

# Show detail url by date.
POST_DETAIL_URL_BY_DATE = getattr(
    settings, 'BLOGIT_POST_DETAIL_URL_BY_DATE', False)

# Url date formats.
URL_YEAR_FORMAT = getattr(settings, 'BLOGIT_URL_YEAR_FORMAT', '%Y')
URL_MONTH_FORMAT = getattr(settings, 'BLOGIT_URL_MONTH_FORMAT', '%m')
URL_DAY_FORMAT = getattr(settings, 'BLOGIT_URL_DAY_FORMAT', '%d')
