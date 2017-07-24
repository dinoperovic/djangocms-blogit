# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from blogit.urls import get_urls

urlpatterns = get_urls('archive') + get_urls('posts')
