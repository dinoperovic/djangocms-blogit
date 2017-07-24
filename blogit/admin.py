# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from cms.admin.placeholderadmin import (FrontendEditableAdminMixin,
                                        PlaceholderAdminMixin)
from django.contrib import admin
from django.contrib.admin.templatetags.admin_static import static
from django.utils import formats
from django.utils.translation import ugettext_lazy as _
from easy_thumbnails.exceptions import InvalidImageFormatError
from easy_thumbnails.files import get_thumbnailer
from mptt.admin import DraggableMPTTAdmin
from parler.admin import TranslatableAdmin

from blogit.models import Category, Post, Tag


class CategoryAdmin(FrontendEditableAdminMixin, PlaceholderAdminMixin, TranslatableAdmin, DraggableMPTTAdmin):
    list_display = ['tree_actions', 'indented_title', 'name', 'slug', 'date_added', 'get_number_of_posts',
                    'language_column']

    list_filter = ['active', 'date_added', 'last_modified', 'translations__language_code']
    readonly_fields = ['date_added', 'last_modified']
    frontend_editable_fields = ['name', 'slug', 'description', 'parent']
    search_fields = ['translations__name']

    fieldsets = [
        (None, {'fields': ['name', 'slug', 'description']}),
        (None, {'fields': ['active', 'date_added', 'last_modified']}),
        (None, {'fields': ['parent']}),
    ]

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ['name']}

    def get_number_of_posts(self, obj):
        return obj.post_set.count()
    get_number_of_posts.short_description = _('Number of Posts')


class TagAdmin(TranslatableAdmin, admin.ModelAdmin):
    list_display = ['name', 'slug', 'date_added', 'get_number_of_posts', 'language_column']
    list_filter = ['active', 'date_added', 'last_modified', 'translations__language_code']
    readonly_fields = ['date_added', 'last_modified']
    frontend_editable_fields = ['name', 'slug', 'description']
    search_fields = ['translations__name']

    fieldsets = [
        (None, {'fields': ['name', 'slug', 'description']}),
        (None, {'fields': ['active', 'date_added', 'last_modified']}),
    ]

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ['name']}

    def get_number_of_posts(self, obj):
        return obj.tagged_posts.count()
    get_number_of_posts.short_description = _('Number of Posts')


class PostAdmin(FrontendEditableAdminMixin, PlaceholderAdminMixin, TranslatableAdmin, admin.ModelAdmin):
    list_display = ['get_title', 'get_slug', 'get_status', 'get_date_published', 'language_column', 'get_image']
    list_filter = ['status', 'date_published', 'date_added', 'last_modified', 'translations__language_code']
    search_fields = ['translations__title']
    readonly_fields = ['date_added', 'last_modified']
    frontend_editable_fields = ['title', 'slug', 'description', 'category', 'author', 'featured_image',
                                'date_published']

    filter_horizontal = ['tags']
    raw_id_fields = ['author']

    fieldsets = [
        (None, {'fields': ['title', 'slug']}),
        (None, {'fields': ['date_added', 'last_modified']}),
        (None, {'fields': ['status', 'date_published']}),
        (None, {'fields': ['featured_image', 'description']}),
        (None, {'fields': ['author', 'category', 'tags']}),
        (_('SEO'), {'fields': ['meta_title', 'meta_description'],
                    'classes': ('collapse',),
                    'description': _('If left blank, fallbacks to the main title and description fields')}),
    ]

    actions = ['make_draft', 'make_private', 'make_public', 'make_hidden']

    class Media:
        css = {'all': ['blogit/css/post_admin.css']}
        js = ['blogit/js/post_admin.js']

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ['title']}

    def get_title(self, obj):
        return obj.name
    get_title.short_description = _('Title')
    get_title.admin_order_field = 'translations__title'

    def get_slug(self, obj):
        return '<a href="{}">{}</a>'.format(obj.get_absolute_url(), obj.safe_translation_getter('slug'))
    get_slug.short_description = _('Slug')
    get_slug.admin_order_field = 'translations__slug'
    get_slug.allow_tags = True

    def get_status(self, obj):
        status_name = dict(Post.STATUS_CODES)[obj.status]
        return '<span class="blogit-status-{}">{}</span>'.format(obj.status, status_name)
    get_status.short_description = _('Status')
    get_status.admin_order_field = 'status'
    get_status.allow_tags = True

    def get_date_published(self, obj):
        if obj.is_published:
            string = '{} <img src="{}/img/icon-yes.gif" alt="True">'
        else:
            string = '{} <img src="{}/img/icon-no.gif" alt="False">'
        date = formats.date_format(obj.date_published, 'SHORT_DATETIME_FORMAT')
        return string.format(date, static('admin'))
    get_date_published.short_description = _('Published on')
    get_date_published.admin_order_field = 'date_published'
    get_date_published.allow_tags = True

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
        except (IOError, ValueError, InvalidImageFormatError):
            return None
    get_image.short_description = _('Image')
    get_image.allow_tags = True

    def message_user_status(self, request, status, rows_updated):
        status_name = dict(Post.STATUS_CODES)[status]
        if rows_updated == 1:
            message_bit = _('1 Post was')
        else:
            message_bit = _('%s Posts were') % rows_updated
        self.message_user(
            request, _('%(posts)s successfully marked as %(status)s.') % {
                'posts': message_bit, 'status': status_name})

    def make_draft(self, request, queryset):
        rows_updated = queryset.update(status=Post.DRAFT)
        self.message_user_status(request, Post.DRAFT, rows_updated)
    make_draft.short_description = _('Mark selected Posts as draft')

    def make_private(self, request, queryset):
        rows_updated = queryset.update(status=Post.PRIVATE)
        self.message_user_status(request, Post.PRIVATE, rows_updated)
    make_private.short_description = _('Mark selected Posts as private')

    def make_public(self, request, queryset):
        rows_updated = queryset.update(status=Post.PUBLIC)
        self.message_user_status(request, Post.PUBLIC, rows_updated)
    make_public.short_description = _('Mark selected Posts as public')

    def make_hidden(self, request, queryset):
        rows_updated = queryset.update(status=Post.HIDDEN)
        self.message_user_status(request, Post.HIDDEN, rows_updated)
    make_hidden.short_description = _('Mark selected Posts as hidden')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
