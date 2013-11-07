# -*- coding: utf-8 -*-
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


BLOGIT_AUTHOR_LINK_TYPE_CHOICES = getattr(settings, 'BLOGIT_AUTHOR_LINK_TYPE_CHOICES', (
    ('', _(u'Custom')),
))
