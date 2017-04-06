Getting started
###############

Get started with installing and configuring **Shopit**.

----

Requirements
============

* Django_ 1.10, 1.9
* django-cms_ for placeholders.
* django-filer_ for file management.
* django-mptt_ for tree management.
* django-parler_ to translate everything.

Installation
============

Install using **pip**:

.. code:: bash

    pip install djangocms-blogit

You should follow django-cms_ & django-filer_ installation guide first, and then add the following to your settings:

.. code:: python

    INSTALLED_APPS = [
        ...
        'mptt',
        'parler',
        'blogit',
    ]

Urls
----

There are two ways to configure the urls. First would be to add to your ``urls.py``:

.. code:: python

    urlpatterns = [
        url(r'^blog/', include('blogit.urls')),
        ...
    ]

The second option is to use django-cms_ apphooks. **Blogit** comes with a couple of those for different application parts. ``BlogitApphook`` is the main one, and one that should always be attached to a page (if the urls are not already added). Then there are other optional apphooks for *category*, *tags* & *feeds*. If you want to keep it simple, and not have to set every application part individually. You can add to your settings:

.. code:: python

    BLOGIT_SINGLE_APPHOOK = True

This will load all the neccesary urls under the ``BlogitApphook``.


.. _Django: https://www.djangoproject.com/
.. _django-cms: https://github.com/divio/django-cms
.. _django-filer: https://github.com/divio/django-filer
.. _django-mptt: https://github.com/django-mptt/django-mptt
.. _django-parler: https://github.com/django-parler/django-parler
