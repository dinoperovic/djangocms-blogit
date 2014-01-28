# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url, patterns, include


urlpatterns = patterns(
    '',
    url(r'^', include('blogit.urls')),
)
