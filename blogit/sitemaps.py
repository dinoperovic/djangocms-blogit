# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.sitemaps import Sitemap

from blogit.models import Post
from blogit import settings as bs


class BlogitSitemap(Sitemap):
    priority = bs.SITEMAP_PRIORITY
    changefreq = bs.SITEMAP_CHANGEFREQ

    def items(self):
        return Post.objects.public().published()

    def lastmod(self, obj):
        return obj.last_modified
