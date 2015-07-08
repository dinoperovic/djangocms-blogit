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
    BLOGIT_FEED_ITEM_AUTHOR_NAME = None  # When none displays author info
    BLOGIT_FEED_ITEM_AUTHOR_EMAIL = None  # When none displays author info
    BLOGIT_FEED_ITEM_DESCRIPTION_FULL = False


Pagination
**********
Pagination per page::

    BLOGIT_POSTS_PER_PAGE = 5


Post url
********

By default post detail url is ``/<post_slug>/``. If you want to have a dated
url like this ``/<year>/<month>/<day>/<post_slug>/``, change this setting::

    BLOGIT_POST_DETAIL_DATE_URL = False
