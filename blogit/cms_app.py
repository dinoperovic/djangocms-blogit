# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

from blogit import settings as bs
from blogit.urls import get_urls


class BlogitApphook(CMSApp):
    name = _('Blogit')
    urls = [get_urls('archive'), get_urls('posts')]

    def __init__(self):
        super(BlogitApphook, self).__init__()
        if bs.SINGLE_APPHOOK:
            self.urls = ['blogit.urls']


class BlogitCategoriesApphook(CMSApp):
    name = _('Blogit Categories')
    urls = [get_urls('categories')]


class BlogitTagsApphook(CMSApp):
    name = _('Blogit Tags')
    urls = [get_urls('tags')]


class BlogitFeedsApphook(CMSApp):
    name = _('Blogit Feeds')
    urls = [get_urls('feeds')]


apphook_pool.register(BlogitApphook)
apphook_pool.register(BlogitCategoriesApphook)
apphook_pool.register(BlogitTagsApphook)
apphook_pool.register(BlogitFeedsApphook)
