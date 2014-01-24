# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import get_language
from django.http import Http404


def get_translation(default, translation, language=None):
    # Returns the correct translation for the given list of tuples.
    if not language:
        language = get_language()

    if translation:
        for item in translation:
            if item[0] == language:
                return item[1]

    return default


def get_translation_regex(default, translation):
    # Returns translation match regex.
    if translation:
        return r'({}|{})'.format(
            default, '|'.join([item[1] for item in translation]))
    return default


def check_translation_or_404(default, translation, value):
    # Raise 404 if translation doesn't match the value.
    if get_translation(default, translation) != value:
        raise Http404()
