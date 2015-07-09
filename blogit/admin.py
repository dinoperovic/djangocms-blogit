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
        'title', 'slug', 'category', 'author', 'get_status', 'date_published',
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

    actions = ['make_draft', 'make_private', 'make_public', 'make_hidden']

    class Media:
        css = {'all': ('blogit/css/blogit.css', ) }
        js = ('blogit/js/admin_post.js', )

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('title', )}

    def get_status(self, obj):
        status_name = dict(Post.STATUS_CODES)[obj.status]
        return '<span class="blogit-status-{}">{}</span>'.\
            format(obj.status, status_name)
    get_status.short_description = _('Status')
    get_status.admin_order_field = 'status'
    get_status.allow_tags = True

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
