# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.contrib.syndication.views import Feed
from django.shortcuts import get_object_or_404
from django.utils.feedgenerator import Rss201rev2Feed, Atom1Feed
from django.utils.encoding import force_text
from django.utils.html import escape

from taggit.models import Tag

from blogit import settings as bs
from blogit.models import Post


# Post Rss feed.
class PostRssFeed(Feed):
    feed_type = Rss201rev2Feed

    def get_object(self, request, tag_slug=None):
        # Returns Tag object with 'tag_slug' passed in from the urls.py
        if tag_slug:
            return get_object_or_404(Tag, slug=tag_slug)
        return None

    def title(self, obj=None):
        title = escape(force_text(bs.TITLE))
        return '{}: {}'.format(title, obj.title) if obj else title

    def description(self):
        return force_text(bs.DESCRIPTION)

    def link(self):
        return reverse('blogit_post_list')

    def items(self, obj=None):
        if obj:
            items = Post.objects.language().published(tags=obj)
        else:
            items = Post.objects.language().published()
        return items[:bs.FEED_LIMIT]

    def item_description(self, item):
        return force_text(item.safe_translation_getter('description'))

    def item_author_email(self, item):
        if item.author:
            return item.author.email
        return None

    def item_author_name(self, item):
        if item.author:
            return item.author.get_full_name()
        return None

    def item_pubdate(self, item):
        return item.date_published


# Post Atom feed.
class PostAtomFeed(PostRssFeed):
    feed_type = Atom1Feed
    subtitle = PostRssFeed.description
