Settings
########


Info
**********

Thease settings are used to render the proper values in feeds.
::
    BLOGIT_TITLE = 'Blogit'
    BLOGIT_DESCRIPTION = 'This is a blog about everything'


Feeds
*****

Feeds can be accessed on ``/<BLOGIT_FEED_URL>/rss/`` and
``/<BLOGIT_FEED_URL>/atom/`` by default. Update feeds using thease settings::

    BLOGIT_RSS_FEED = True
    BLOGIT_ATOM_FEED = True
    BLOGIT_FEED_LIMIT = 100
    BLOGIT_FEED_URL = 'feeds'

.. Note::
    ``BLOGIT_FEED_URL`` value should be slugified. (Use dashes and underscores
    for spaces, and no special characters).


Pagination
**********
Pagination per page::

    BLOGIT_POSTS_PER_PAGE = 5


Post url
********

By default post detail url is ``/<post_slug>/``. If you want to have a dated
url like this ``/<year>/<month>/<day>/<post_slug>/``, change this setting::

    BLOGIT_POST_DETAIL_DATE_URL = False
