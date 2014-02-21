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

Set how many items are displayed per page::

    BLOGIT_AUTHORS_PER_PAGE = 5
    BLOGIT_CATEGORIES_PER_PAGE = 5
    BLOGIT_TAGS_PER_PAGE = 5
    BLOGIT_POSTS_PER_PAGE = 5


Templates
*********

Update default templates with thease settings::

    BLOGIT_AUTHOR_LIST_TEMPLATE = 'blogit/author/list.html'
    BLOGIT_AUTHOR_DETAIL_TEMPLATE = 'blogit/author/detail.html'

    BLOGIT_CATEGORY_LIST_TEMPLATE = 'blogit/category/list.html'
    BLOGIT_CATEGORY_DETAIL_TEMPLATE = 'blogit/category/detail.html'

    BLOGIT_TAG_LIST_TEMPLATE = 'blogit/tag/list.html'
    BLOGIT_TAG_DETAIL_TEMPLATE = 'blogit/tag/detail.html'

    BLOGIT_POST_LIST_TEMPLATE = 'blogit/list.html'
    BLOGIT_POST_DETAIL_TEMPLATE = 'blogit/detail.html'

    BLOGIT_ARCHIVE_LIST_TEMPLATE = POST_LIST_TEMPLATE


Choices
*******

Empty by default. Set choices by specifying a list of tuples::

    BLOGIT_AUTHOR_LINK_TYPE_CHOICES = (
        ('google', 'Google'),
        ('facebook', 'Facebook'),
        ('twitter', 'Twitter'),
    )


Url translation
***************

If url translation for a language is not specified, it will fallback to their
default value. You can update the default values using thease settings::

    BLOGIT_AUTHOR_URL = 'authors'
    BLOGIT_CATEGORY_URL = 'categories'
    BLOGIT_TAG_URL = 'tags'

To translate an url, set a value for the language you want like this (Empty by
default)::

    BLOGIT_AUTHOR_URL_TRANSLATION = (
        ('en', 'authors'),
        ('hr', 'autori'),
    )
    BLOGIT_CATEGORY_URL_TRANSLATION = (
        ('en', 'categories'),
        ('hr', 'kategorije'),
    )
    BLOGIT_TAG_URL_TRANSLATION = (
        ('en', 'tags'),
        ('hr', 'tagovi'),
    )


.. note::
    When setting url translations, make sure the ``language_code`` part
    reflects the laguage specified in your ``settings.LANGUAGES``. Since you
    are translating an url, make sure your input is slugified. (Use dashes and
    underscores for spaces, and no special characters).


Post url
********

By default post detail url is ``/<post_slug>/``. If you want to have a dated
url like this ``/<year>/<month>/<day>/<post_slug>/``, change this setting::

    BLOGIT_POST_DETAIL_URL_BY_DATE = False


Url date format
***************

Date formats used in dated urls, Must be a valid date formatting code::

    BLOGIT_URL_YEAR_FORMAT = '%Y'
    BLOGIT_URL_MONTH_FORMAT = '%m'
    BLOGIT_URL_DAY_FORMAT = '%d'



Disable urls
************

If you want to disable an url, change thease settings::

    BLOGIT_ADD_AUTHOR_URLS = True
    BLOGIT_ADD_CATEGORY_URLS = True
    BLOGIT_ADD_TAG_URLS = True
    BLOGIT_ADD_ARCHIVE_URLS = True
