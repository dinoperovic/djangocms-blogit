# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

from blogit import views, settings, utils


CATEGORY_URLS = '(category|{})'.format('|'.join([item[1] for item in settings.BLOGIT_CATEGORY_URL_TRANSLATIONS]))
AUTHOR_URLS = '(author|{})'.format('|'.join([item[1] for item in settings.BLOGIT_AUTHOR_URL_TRANSLATIONS]))

urlpatterns = patterns('',
    url(r'^$', views.post_list, name='blogit_list'),
    url(r'^(?P<category_url>{})/(?P<category_slug>[-\w\d]+)/$'.format(CATEGORY_URLS), views.category_list, name='blogit_category'),
    url(r'^(?P<author_url>{})/(?P<author_slug>[-\w\d]+)$'.format(AUTHOR_URLS), views.author_list, name='blogit_author'),
    url(r'^(?P<post_slug>[-\w\d]+)/$', views.single, name='blogit_single'),
)
