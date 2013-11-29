# -*- coding: utf-8 -*-
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

# Use AUTH_USER_MODEL as user.
AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

# How many posts per page are displayed.
BLOGIT_POSTS_PER_PAGE = getattr(settings, 'BLOGIT_POSTS_PER_PAGE', 5)

# Choices.
BLOGIT_AUTHOR_LINK_TYPE_CHOICES = getattr(settings, 'BLOGIT_AUTHOR_LINK_TYPE_CHOICES', ())

# Url translations.
BLOGIT_CATEGORY_URL_TRANSLATIONS = getattr(settings, 'BLOGIT_CATEGORY_URL_TRANSLATIONS', ())
BLOGIT_AUTHOR_URL_TRANSLATIONS = getattr(settings, 'BLOGIT_CATEGORY_URL_TRANSLATIONS', ())
