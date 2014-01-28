# -*- coding: utf-8 -*-
from __future__ import unicode_literals


LANGUAGE_CODE = 'en'
LANGUAGES = [
    ('en', 'English'),
    ('hr', 'Hrvatski'),
]

DEBUG = True
TEMPLATE_DEBUG = True

ROOT_URLCONF = 'tests.urls'

SECRET_KEY = 'secretkey'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

STATIC_URL = '/static/'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.admin',
    'cms',
    'cms.plugins.text',
    'mptt',
    'easy_thumbnails',
    'filer',
    'hvad',
    'taggit',
    'blogit',
    'tests',
)

BLOGIT_AUTHOR_URL_TRANSLATION = (
    ('en', 'authors'),
    ('hr', 'autori'),
)
BLOGIT_CATEGORY_URL_TRANSLATION = (
    ('en', 'categories'),
    ('hr', 'kategorije'),
)
BLOGIT_TAG_URL_TRANSLATION = (
    ('en', 'tags'),
    ('hr', 'tagovi'),
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)
