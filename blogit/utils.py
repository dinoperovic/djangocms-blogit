# -*- coding: utf-8 -*-
from django.utils.translation import get_language
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

        return translation[0][1]
    else:
        return default


def get_translation_regex(default, translation):
    # Returns translation match regex.
    if translation:
        return '({}|{})'.format(
            default, '|'.join([item[1] for item in translation]))
    else:
        return default
