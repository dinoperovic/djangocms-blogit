# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

from blogit import views


urlpatterns = patterns('',
    url(r'^$', views.list, name='blogit_list'),
    url(r'^(?P<category_url>[-\w\d]+)/(?P<category_slug>[-\w\d]+)$', views.list, name='blogit_category'),
    url(r'^(?P<post_slug>[-\w\d]+)$', views.single, name='blogit_single'),
)