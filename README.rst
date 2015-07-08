================
djangocms-blogit
================

A simple blog app for `django-cms`_.

:Version: 0.3.8
:Download: http://pypi.python.org/pypi/djangocms-blogit/
:Source: http://github.com/dinoperovic/djangocms-blogit/
:Docs: http://djangocms-blogit.readthedocs.org/
:Dev Status: Alpha


Dependencies
############

* `django-cms`_ >= 3.0.0
* `django-filer`_ >= 0.9.5
* `django-parler`_ >= 1.4
* `django-taggit`_ >= 0.10

Installation
############

To install ``djangocms-blogit`` with ``pip`` run::

    $ pip install djangocms-blogit


Setup
#####

Setup `django-cms`_ and `django-filer`_ than add to ``INSTALLED_APPS``:

.. code:: python

    INSTALLED_APPS = (
        ...
        'parler',
        'taggit',
        'blogit',
        ...
    )


Settings
########
You can browse all the setings in a `settings.py`_ file.


Important
#########

Backwards incompatible with versions below 0.3.0



.. _settings.py: https://github.com/dinoperovic/djangocms-blogit/blob/master/blogit/settings.py
.. _django-cms: https://github.com/divio/django-cms
.. _django-filer: https://github.com/stefanfoulis/django-filer
.. _django-parler: https://github.com/edoburu/django-parler
.. _django-taggit: https://github.com/alex/django-taggit
