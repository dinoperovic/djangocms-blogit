# -*- coding: utf-8 -*-
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
