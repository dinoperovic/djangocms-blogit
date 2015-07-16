# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory
from django.template import RequestContext
from django.utils.html import strip_tags
try:
    from django.utils.encoding import force_unicode
except ImportError:
    from django.utils.encoding import force_text as force_unicode

from cms.utils.i18n import get_current_language


def get_request(language=None):
    """
    Returns a Request instance populated with cms specific attributes
    """
    request_factory = RequestFactory()
    request = request_factory.get('/')
    request.session = {}
    request.LANGUAGE_CODE = language or settings.LANGUAGE_CODE
    request.current_page = None
    request.user = AnonymousUser()
    return request


def get_text_from_placeholder(placeholder, language=None, request=None):
    """
    Returns rendered and strippet text from given placeholder
    """
    if not placeholder:
        return ''
    if not language:
        language = get_current_language()
    if not request:
        request = get_request(language)

    bits = []
    plugins = placeholder.cmsplugin_set.filter(language=language)
    for base_plugin in plugins:
        instance, plugin_type = base_plugin.get_plugin_instance()
        if instance is None:
            continue
        bits.append(instance.render_plugin(context=RequestContext(request)))
    return force_unicode(strip_tags(' '.join(bits)))
