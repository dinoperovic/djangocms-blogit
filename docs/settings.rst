Settings
########


Info
====

Thease settings are used to render the proper values in feeds:

.. code:: python

    BLOGIT_TITLE = 'Blogit'
    BLOGIT_DESCRIPTION = 'This is a blog about everything'


Feeds
=====

.. code:: python

    BLOGIT_FEED_LIMIT = 100
    BLOGIT_FEED_ITEM_AUTHOR_NAME = None  # When none displays author info
    BLOGIT_FEED_ITEM_AUTHOR_EMAIL = None  # When none displays author info
    BLOGIT_FEED_ITEM_DESCRIPTION_FULL = False
    BLOGIT_FEED_DEFAULT = 'rss'  # [rss|atom]


Pagination
==========

Pagination per page:

.. code:: python

    BLOGIT_POSTS_PER_PAGE = 5

Post url
========

By default post detail url is ``/<post_slug>/``. If you want to have a dated
url like this ``/<year>/<month>/<day>/<post_slug>/``, change this setting:

.. code:: python

    BLOGIT_POST_DETAIL_DATE_URL = False
