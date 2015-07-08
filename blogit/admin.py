# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from easy_thumbnails.files import get_thumbnailer
from parler.admin import TranslatableAdmin
from cms.admin.placeholderadmin import (
    PlaceholderAdminMixin, FrontendEditableAdminMixin)

from blogit.models import Category, Tag, Post


class CategoryAdmin(FrontendEditableAdminMixin, PlaceholderAdminMixin,
                    TranslatableAdmin, admin.ModelAdmin):

    list_display = (
        'name', 'slug', 'date_added', 'get_number_of_posts', 'language_column')

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
        return Post.objects.translated().published(category=obj).count()
    get_number_of_posts.short_description = _('Number of Posts')


class TagAdmin(TranslatableAdmin, admin.ModelAdmin):
    list_display = (
        'name', 'slug', 'date_added', 'get_number_of_posts', 'language_column')

    list_filter = ('active', 'date_added', 'last_modified')
    readonly_fields = ('date_added', 'last_modified')
    frontend_editable_fields = ('name', 'slug', 'description', )

    declared_fieldsets = (
        (None, {'fields': ('name', 'slug', 'description')}),
        (None, {'fields': ('active', 'date_added', 'last_modified')}),
    )

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name', )}

    def get_number_of_posts(self, obj):
        return obj.tagged_posts.count()
    get_number_of_posts.short_description = _('Number of Posts')


class PostAdmin(FrontendEditableAdminMixin, PlaceholderAdminMixin,
                TranslatableAdmin, admin.ModelAdmin):

    list_display = (
        'title', 'slug', 'category', 'author', 'status', 'date_published',
        'language_column', 'get_image')

    list_filter = (
        'status', 'date_published', 'date_added', 'last_modified',
        'category', 'author')

    readonly_fields = ('date_added', 'last_modified')

    frontend_editable_fields = (
        'title', 'slug', 'description', 'category', 'author',
        'featured_image', 'date_published')

    filter_horizontal = ('tags', )

    raw_id_fields = ('author', )

    declared_fieldsets = (
        (None, {'fields': ('title', 'slug')}),
        (None, {'fields': ('date_added', 'last_modified')}),
        (None, {'fields': ('status', 'date_published')}),
        (None, {'fields': ('featured_image', 'description')}),
        (None, {'fields': ('author', 'category', 'tags')}),
        (_('SEO'), {'fields': ('meta_title', 'meta_description'),
                    'classes': ('collapse',),
                    'description': _('If left blank, fallbacks to the main '
                                     'title and description fields')}),
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
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
