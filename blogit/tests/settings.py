# -*- coding: utf-8 -*-
from __future__ import unicode_literals


LANGUAGE_CODE = 'en'
LANGUAGES = [
    ('en', 'English'),
    ('hr', 'Hrvatski'),
]

DEBUG = True
TEMPLATE_DEBUG = True

ROOT_URLCONF = 'blogit.tests.urls'

SECRET_KEY = 'secretkey'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.contenttypes',
    'django.contrib.admin',
    'djangocms_text_ckeditor',
    'cms',
    'mptt',
    'easy_thumbnails',
    'filer',
    'hvad',
    'taggit',
    'blogit',
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
