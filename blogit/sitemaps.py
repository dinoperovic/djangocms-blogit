# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.sitemaps import Sitemap

from blogit.models import Post


class BlogitSitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return Post.objects.translated().published()

    def lastmod(self, obj):
        return obj.last_modified
