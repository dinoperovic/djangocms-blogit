# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from easy_thumbnails.files import get_thumbnailer
from parler.admin import TranslatableAdmin
from cms.admin.placeholderadmin import (
    PlaceholderAdminMixin, FrontendEditableAdminMixin)

from blogit.models import Category, Post


class CategoryAdmin(FrontendEditableAdminMixin, PlaceholderAdminMixin,
                    TranslatableAdmin, admin.ModelAdmin):

    list_display = (
        'name', 'slug', 'date_added', 'get_number_of_posts',
        'language_column')

    list_filter = ('active', 'date_added', 'last_modified')
    readonly_fields = ('date_added', 'last_modified')
    frontend_editable_fields = ('name', 'slug', 'description', 'parent')

    declared_fieldsets = (
        (None, {'fields': ('name', 'slug', 'description')}),
        (None, {'fields': ('active', 'date_added', 'last_modified')}),
        (None, {'fields': ('parent', )}),
    )

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name', )}

    def get_number_of_posts(self, obj):
        return Post.objects.language().published(category=obj).count()
    get_number_of_posts.short_description = _('Number of Posts')


class PostAdmin(FrontendEditableAdminMixin, PlaceholderAdminMixin,
                TranslatableAdmin, admin.ModelAdmin):

    list_display = (
        'title', 'slug', 'category', 'author', 'date_published',
        'language_column', 'get_image')

    list_filter = (
        'active', 'date_published', 'date_added', 'last_modified',
        'category', 'author')

    readonly_fields = ('date_added', 'last_modified')

    frontend_editable_fields = (
        'title', 'slug', 'description', 'category', 'author',
        'featured_image', 'date_published')

    declared_fieldsets = (
        (None, {'fields': ('title', 'slug')}),
        (None, {'fields': (
            'active', 'date_added', 'last_modified', 'date_published')}),
        (None, {'fields': ('description', 'tags')}),
        (None, {'fields': ('author', 'category', 'featured_image')}),
    )

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('title', )}

    def get_image(self, obj):
        try:
            options = {
                'size': [72, 72],
                'crop': True,
                'upscale': True,
            }
            thumbnailer = get_thumbnailer(obj.featured_image)
            thumb = thumbnailer.get_thumbnail(options)
            return '<img src="{}">'.format(thumb.url)
        except (IOError, ValueError):
            return None
    get_image.short_description = _('Featured Image')
    get_image.allow_tags = True


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
