# -*- coding: utf-8 -*-
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

BLOGIT_AUTHOR_LINK_TYPE_CHOICES = getattr(settings, 'BLOGIT_AUTHOR_LINK_TYPE_CHOICES', ())
BLOGIT_CATEGORY_URL_TRANSLATIONS = getattr(settings, 'BLOGIT_CATEGORY_URL_TRANSLATIONS', ())
BLOGIT_AUTHOR_URL_TRANSLATIONS = getattr(settings, 'BLOGIT_CATEGORY_URL_TRANSLATIONS', ())
