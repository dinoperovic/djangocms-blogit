# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.contrib.syndication.views import Feed
from django.shortcuts import get_object_or_404
from django.utils.feedgenerator import Rss201rev2Feed, Atom1Feed
from django.utils.encoding import force_text
from django.utils.html import escape

from blogit import settings as bs
from blogit.models import Post, Tag


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
        return '{}: {}'.format(title, obj.name) if obj else title

    def description(self):
        return force_text(bs.DESCRIPTION)

    def link(self):
        return reverse('blogit_post_list')

    def items(self, obj=None):
        if obj:
            items = Post.objects.public().filter(tags=obj)
        else:
            items = Post.objects.public()
        return items.order_by('-date_published')[:bs.FEED_LIMIT]

    def item_description(self, item):
        return force_text(item.lazy_translation_getter('description'))

    def item_author_email(self, item):
        return item.author.get_email()

    def item_author_name(self, item):
        return item.author.get_full_name()

    def item_author_link(self, item):
        return item.author.get_absolute_url()

    def item_pubdate(self, item):
        return item.date_published


# Post Atom feed.
class PostAtomFeed(PostRssFeed):
    feed_type = Atom1Feed
    subtitle = PostRssFeed.description
