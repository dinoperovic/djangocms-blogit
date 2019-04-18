# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.syndication.views import Feed
from django.urls import reverse
from django.utils.feedgenerator import Atom1Feed, Rss201rev2Feed
from django.utils.html import escape

from blogit import settings as bs
from blogit.models import Post, Tag

try:
    from django.utils.encoding import force_unicode
except ImportError:
    from django.utils.encoding import force_text as force_unicode


# Post Rss feed.
class PostRssFeed(Feed):
    feed_type = Rss201rev2Feed

    def get_object(self, request, slug=None):
        # Returns Tag object with 'slug' passed in from the urls.py
        if slug:
            try:
                return Tag.objects.translated(slug=slug).get()
            except Tag.DoesNotExist:
                pass
        return None

    def title(self, obj=None):
        title = escape(force_unicode(bs.TITLE))
        return '{}: {}'.format(title, obj.name) if obj else title

    def description(self):
        return force_unicode(bs.DESCRIPTION)

    def link(self):
        return reverse('blogit_post_list')

    def items(self, obj=None):
        filters = {}
        if obj:
            filters['tags'] = obj
        return Post.objects.public().published(**filters)[:bs.FEED_LIMIT]

    def item_description(self, item):
        if bs.FEED_ITEM_DESCRIPTION_FULL:
            # TODO: render all text plugins from body placeholder
            pass
        return force_unicode(item.safe_translation_getter('description'))

    def item_author_email(self, item):
        if bs.FEED_ITEM_AUTHOR_EMAIL is not None:
            return bs.FEED_ITEM_AUTHOR_EMAIL
        if item.author:
            return item.author.email
        return None

    def item_author_name(self, item):
        if bs.FEED_ITEM_AUTHOR_NAME is not None:
            return bs.FEED_ITEM_AUTHOR_NAME
        if item.author:
            return item.author.get_full_name()
        return None

    def item_pubdate(self, item):
        return item.date_published


# Post Atom feed.
class PostAtomFeed(PostRssFeed):
    feed_type = Atom1Feed
    subtitle = PostRssFeed.description
