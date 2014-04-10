================
djangocms-blogit
================

A simple blog app for `django-cms`_.

:Version: 0.1.1
:Docs: http://djangocms-blogit.readthedocs.org/
:Download: http://pypi.python.org/pypi/djangocms-blogit/
:Source: http://github.com/dinoperovic/djangocms-blogit/
:Dev Status: Alpha


Dependencies
------------

* `django-cms`_ == 2.4.3
* `django-filer`_ == 0.9.5
* `django-hvad`_ == 0.3
* `django-taggit`_ == 0.10

Installation
------------

To install ``djangocms-blogit`` with ``pip`` run::

    $ pip install djangocms-blogit


Setup
-------------

Setup `django-cms`_ and `django-filer`_ than add to ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...
        'hvad',
        'taggit',
        'blogit',
        ...
    )


Settings
-------------
You can browse all the setings in a `settings.py`_ file.

**Url translation example**::

    BLOGIT_CATEGORY_URL_TRANSLATION = (
        ('en', 'category'),
        ('hr', 'kategorija'),
        ...
    )


Versions
-------------
0.1.0 - Alpha release
    To migrate from earlier versions using south run **(some fields may be lost)**::

        $ pip install --upgrade djangocms-blogit==0.0.99
        $ python manage.py migrate blogit
        $ pip install --upgrade djangocms-blogit==0.1.0
        $ python manage.py migrate blogit 0001 --fake --delete-ghost-migrations



.. _settings.py: https://github.com/dinoperovic/djangocms-blogit/blob/master/blogit/settings.py
.. _django-cms: https://github.com/divio/django-cms
.. _django-filer: https://github.com/stefanfoulis/django-filer
.. _django-hvad: https://github.com/kristianoellegaard/django-hvad
.. _django-taggit: https://github.com/alex/django-taggit
