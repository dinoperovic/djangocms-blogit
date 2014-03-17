# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _


# Basic info (used in feeds).
TITLE = getattr(settings, 'BLOGIT_TITLE', _('Blogit'))
DESCRIPTION = getattr(
    settings, 'BLOGIT_DESCRIPTION', _('This is a blog about everything'))


# User model.
AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


# Feeds.
RSS_FEED = getattr(settings, 'BLOGIT_RSS_FEED', True)
ATOM_FEED = getattr(settings, 'BLOGIT_ATOM_FEED', True)
FEED_LIMIT = getattr(settings, 'BLOGIT_FEED_LIMIT', 100)
FEED_URL = getattr(settings, 'BLOGIT_FEED_URL', 'feeds')


# How many items per page are displayed.
ITEMS_PER_PAGE = getattr(settings, 'BLOGIT_ITEMS_PER_PAGE', 6)
AUTHORS_PER_PAGE = getattr(settings, 'BLOGIT_AUTHORS_PER_PAGE', ITEMS_PER_PAGE)
CATEGORIES_PER_PAGE = getattr(
    settings, 'BLOGIT_CATEGORIES_PER_PAGE', ITEMS_PER_PAGE)
TAGS_PER_PAGE = getattr(
    settings, 'BLOGIT_TAGS_PER_PAGE', ITEMS_PER_PAGE)
POSTS_PER_PAGE = getattr(
    settings, 'BLOGIT_POSTS_PER_PAGE', ITEMS_PER_PAGE)


# Templates.
AUTHOR_LIST_TEMPLATE = getattr(
    settings, 'BLOGIT_AUTHOR_LIST_TEMPLATE', 'blogit/author/list.html')
AUTHOR_DETAIL_TEMPLATE = getattr(
    settings, 'BLOGIT_AUTHOR_DETAIL_TEMPLATE', 'blogit/author/detail.html')

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


# Enable urls.
ADD_AUTHOR_URLS = getattr(settings, 'BLOGIT_ADD_AUTHOR_URLS', True)
ADD_CATEGORY_URLS = getattr(settings, 'BLOGIT_ADD_CATEGORY_URLS', True)
ADD_TAG_URLS = getattr(settings, 'BLOGIT_ADD_TAG_URLS', True)
ADD_ARCHIVE_URLS = getattr(settings, 'BLOGIT_ADD_ARCHIVE_URLS', True)


# Show detail url by date.
POST_DETAIL_URL_BY_DATE = getattr(
    settings, 'BLOGIT_POST_DETAIL_URL_BY_DATE', False)


# Url date formats.
URL_YEAR_FORMAT = getattr(settings, 'BLOGIT_URL_YEAR_FORMAT', '%Y')
URL_MONTH_FORMAT = getattr(settings, 'BLOGIT_URL_MONTH_FORMAT', '%m')
URL_DAY_FORMAT = getattr(settings, 'BLOGIT_URL_DAY_FORMAT', '%d')
