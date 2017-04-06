# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

from blogit import settings as bs

# TODO: can be simplified into, after merging https://github.com/divio/django-cms/pull/5898
# from blogit.urls import get_urls

# def get_urls(self, page=None, language=None, **kwargs):
#     return get_urls('module')


class BlogitApphook(CMSApp):
    name = _('Blogit')

    def get_urls(self, page=None, language=None, **kwargs):
        if bs.SINGLE_APPHOOK:
            return ['blogit.urls']
        return ['blogit.urls.archive_posts']


class BlogitCategoriesApphook(CMSApp):
    name = _('Blogit Categories')

    def get_urls(self, page=None, language=None, **kwargs):
        return ['blogit.urls.categories']


class BlogitTagsApphook(CMSApp):
    name = _('Blogit Tags')

    def get_urls(self, page=None, language=None, **kwargs):
        return ['blogit.urls.tags']


class BlogitFeedsApphook(CMSApp):
    name = _('Blogit Feeds')

    def get_urls(self, page=None, language=None, **kwargs):
        return ['blogit.urls.feeds']


apphook_pool.register(BlogitApphook)

if not bs.SINGLE_APPHOOK:
    apphook_pool.register(BlogitCategoriesApphook)
    apphook_pool.register(BlogitTagsApphook)
    apphook_pool.register(BlogitFeedsApphook)
