================
cmsplugin-blogit
================

**Project is a development stage (pre-alpha)**

A simple blog plugin for django-cms.

Dependencies
------------

* `django-cms`_ >= 2.4
* `django-mptt`_ == 0.5.5
* `django-hvad`_ == 0.3
* `easy-thumbnails`_ == 1.4
* `django-filer`_ >= 0.9
* `django-taggit`_ == 0.10

Installation
------------

To install ``cmsplugin-blogit`` with ``pip`` run::

    $ pip install cmsplugin-blogit


Setup
-------------

Setup `django-cms`_ than add to ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...
        'hvad',
        'easy_thumbnails',
        'filer',
        'taggit',
        'blogit',
        ...
    )


Settings
-------------

BLOGIT_POSTS_PER_PAGE
    Number of posts displayed per page.
    Defaults to 5.

BLOGIT_LIST_TEMPLATE
    Path to list template. Defaults to ``blogit/list.html``

BLOGIT_DETAIL_TEMPLATE
    Path to detail template. Defaults to ``blogit/detail.html``

BLOGIT_AUTHOR_LINK_TYPE_CHOICES
    Link type choices for authors. List of tuples.

BLOGIT_CATEGORY_URL, BLOGIT_AUTHOR_URL
    Default url names.

BLOGIT_CATEGORY_URL_TRANSLATION, BLOGIT_AUTHOR_URL_TRANSLATION
    Url translation.
    ::
        BLOGIT_CATEGORY_URL_TRANSLATION = (
            ('en', 'category'),
            ('hr', 'kategorija'),
            ...
        )


.. _django-cms: https://github.com/divio/django-cms
.. _easy-thumbnails: https://github.com/SmileyChris/easy-thumbnails
.. _django-filer: https://github.com/stefanfoulis/django-filer
.. _django-hvad: https://github.com/kristianoellegaard/django-hvad
.. _django-mptt: https://github.com/django-mptt/django-mptt
.. _django-taggit: https://github.com/alex/django-taggit
