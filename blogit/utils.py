# -*- coding: utf-8 -*-
from django.utils.translation import get_language
from django.http import Http404

from easy_thumbnails.files import get_thumbnailer


def thumb(image, size, crop=True, upscale=True):
    # Returns a thumbnail.
    try:
        options = {
            'size': size.split('x'),
            'crop': crop,
            'upscale': upscale,
        }
        thumbnailer = get_thumbnailer(image)
        thumb = thumbnailer.get_thumbnail(options)
        return thumb.url
    except IOError:
        return None


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
    else:
        return default


def check_translation_or_404(default, translation, value):
    # Raise 404 if translation doesn't match the value.
    if get_translation(default, translation) != value:
        raise Http404()
