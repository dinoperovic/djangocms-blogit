Getting started
###############

Requirements
************

* `django-cms`_ == 2.4.3
* `django-filer`_ == 0.9.5
* `django-hvad`_ == 0.3
* `django-taggit`_ == 0.10


Installation
************

To install ``djangocms-blogit`` with ``pip`` run::

    $ pip install djangocms-blogit


Setup
*****

Setup `django-cms`_ and `django-filer`_ than add to ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...
        'hvad',
        'taggit',
        'blogit',
        ...
    )


.. _django-cms: https://github.com/divio/django-cms
.. _django-filer: https://github.com/stefanfoulis/django-filer
.. _django-hvad: https://github.com/kristianoellegaard/django-hvad
.. _django-taggit: https://github.com/alex/django-taggit
