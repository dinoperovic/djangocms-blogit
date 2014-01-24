# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class BlogitApphook(CMSApp):
    name = _('Blogit')
    urls = ['blogit.urls']


apphook_pool.register(BlogitApphook)
