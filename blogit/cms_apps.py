# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

from blogit import settings as bs
from blogit.urls import get_urls


class BlogitApphook(CMSApp):
    name = _('Blogit')

    def get_urls(self, page=None, language=None, **kwargs):
        if bs.SINGLE_APPHOOK:
            return ['blogit.urls']
        return [get_urls('archive'), get_urls('posts')]


class BlogitCategoriesApphook(CMSApp):
    name = _('Blogit Categories')

    def get_urls(self, page=None, language=None, **kwargs):
        return [get_urls('categories')]


class BlogitTagsApphook(CMSApp):
    name = _('Blogit Tags')

    def get_urls(self, page=None, language=None, **kwargs):
        return [get_urls('tags')]


class BlogitFeedsApphook(CMSApp):
    name = _('Blogit Feeds')

    def get_urls(self, page=None, language=None, **kwargs):
        return [get_urls('feeds')]


apphook_pool.register(BlogitApphook)

if not bs.SINGLE_APPHOOK:
    apphook_pool.register(BlogitCategoriesApphook)
    apphook_pool.register(BlogitTagsApphook)
    apphook_pool.register(BlogitFeedsApphook)
