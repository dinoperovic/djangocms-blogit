# -*- coding: utf-8 -*-
from django.conf import settings


# Use AUTH_USER_MODEL as user.
AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

# How many posts per page are displayed.
POSTS_PER_PAGE = getattr(settings, 'BLOGIT_POSTS_PER_PAGE', 5)

# Templates.
LIST_TEMPLATE = getattr(settings, 'BLOGIT_LIST_TEMPLATE', 'blogit/list.html')
DETAIL_TEMPLATE = getattr(
    settings, 'BLOGIT_DETAIL_TEMPLATE', 'blogit/detail.html')

# Choices.
AUTHOR_LINK_TYPE_CHOICES = getattr(
    settings, 'BLOGIT_AUTHOR_LINK_TYPE_CHOICES', ())

# Urls and translations.
CATEGORY_URL = getattr(settings, 'BLOGIT_CATEGORY_URL', 'category')
CATEGORY_URL_TRANSLATION = getattr(
    settings, 'BLOGIT_CATEGORY_URL_TRANSLATION', ())

AUTHOR_URL = getattr(settings, 'BLOGIT_AUTHOR_URL', 'author')
AUTHOR_URL_TRANSLATION = getattr(
    settings, 'BLOGIT_AUTHOR_URL_TRANSLATION', ())
