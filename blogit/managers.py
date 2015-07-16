# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils import timezone

from parler.managers import TranslatableManager, TranslatableQuerySet


class PostQuerySet(TranslatableQuerySet):
    def published(self, **kwargs):
        return self.filter(date_published__lte=timezone.now, **kwargs)


class PostManager(TranslatableManager):
    queryset_class = PostQuerySet

    def published(self, request, **kwargs):
        queryset = self.public(**kwargs).published()
        if hasattr(request, 'user') and request.user.is_authenticated():
            if request.user.is_staff:
                queryset = queryset | self.draft(**kwargs)
            queryset = queryset | self.private(request.user, **kwargs)
        return queryset

    def draft(self, **kwargs):
        return self.get_queryset().filter(status=0, **kwargs)

    def private(self, user, **kwargs):
        return self.get_queryset().filter(status=1, author=user, **kwargs)

    def public(self, **kwargs):
        return self.get_queryset().filter(status=2, **kwargs)

    def hidden(self, **kwargs):
        return self.get_queryset().filter(status=3, **kwargs)
