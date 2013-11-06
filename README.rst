================
cmsplugin-blogit
================

**Project is a development stage (pre-alpha)**

A simple blog plugin for django-cms.

Dependencies
------------

* `django-cms`_ >= 2.4
* `easy_thumbnails`_ 1.3
* `django-filer`_ >= 0.9
* `django-hvad`_ 0.3
* `django-taggit`_ 0.10

Installation
------------

To install ``cmsplugin-blogit`` with ``pip`` run::

    $ pip install cmsplugin-blogit


Configuration
-------------

Install `django-cms`_ and add to ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...
        'hvad',
        'easy_thumbnails',
        'filer',
        'taggit',
        'blogit',
        ...
    )


.. _django-cms: https://github.com/divio/django-cms
.. _easy_thumbnails: https://github.com/SmileyChris/easy-thumbnails
.. _django-filer: https://github.com/stefanfoulis/django-filer
.. _django-hvad: https://github.com/kristianoellegaard/django-hvad
.. _django-taggit: https://github.com/alex/django-taggit
