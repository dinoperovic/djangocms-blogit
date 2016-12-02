Getting started
###############

Installation
============

To install with **pip** run:

.. code:: bash

    pip install djangocms-blogit

Configuration
=============

Setup `django-cms`_ and then add to settings:

.. code:: python

    INSTALLED_APPS = [
        ...
        'mptt',
        'parler',
        'blogit',
    ]


.. _django-cms: https://github.com/divio/django-cms
