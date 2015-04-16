# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _


ACTIVE_FIELD_HELP_TEXT = _('Is this object active?')


# Basic info (used in feeds).
TITLE = getattr(settings, 'BLOGIT_TITLE', _('Blogit'))
DESCRIPTION = getattr(
    settings, 'BLOGIT_DESCRIPTION', _('This is a blog about everything'))


# Feeds.
RSS_FEED = getattr(settings, 'BLOGIT_RSS_FEED', True)
ATOM_FEED = getattr(settings, 'BLOGIT_ATOM_FEED', True)
FEED_LIMIT = getattr(settings, 'BLOGIT_FEED_LIMIT', 100)
FEED_URL = getattr(settings, 'BLOGIT_FEED_URL', 'feeds')


# How many posts per page are displayed.
POSTS_PER_PAGE = getattr(settings, 'BLOGIT_POSTS_PER_PAGE', 10)


# Url strings.
CATEGORY_URL = getattr(settings, 'BLOGIT_CATEGORY_URL', 'categories')


# Show detail url by date.
POST_DETAIL_DATE_URL = getattr(
    settings, 'BLOGIT_POST_DETAIL_DATE_URL', False)
