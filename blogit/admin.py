# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from mptt.admin import MPTTModelAdmin
from hvad.admin import TranslatableAdmin
from cms.admin.placeholderadmin import PlaceholderAdmin

from blogit.models import AuthorLink, Author, Category, Tag, TaggedPost, Post


class AuthorLinkInline(admin.TabularInline):
    model = AuthorLink
    extra = 0


class AuthorAdmin(TranslatableAdmin, PlaceholderAdmin):
    list_display = ('__unicode__', 'slug', 'all_translations', 'admin_image')
    inlines = (AuthorLinkInline,)

    def __init__(self, *args, **kwargs):
        super(AuthorAdmin, self).__init__(*args, **kwargs)
        self.fieldsets = (
            (None, {
                'fields': ('slug', 'user'),
                'description': _(
                    'These fields are the same across all languages.'),
            }),
            (_('Personal Info'), {
                'fields': ('first_name', 'last_name', 'email', 'picture'),
                'description': _(
                    'These fields are the same across all languages.'),
            }),
            (None, {
                'fields': ('description',),
            }),
            (None, {
                'fields': ('bio',),
            }),
        )


class CategoryAdmin(TranslatableAdmin, PlaceholderAdmin, MPTTModelAdmin):
    list_display = (
        'title_', 'slug_', 'date_created', 'last_modified',
        'all_translations')
    list_filter = ('date_created', 'last_modified')
    readonly_fields = ('last_modified',)
    mptt_indent_field = 'title_'

    def __init__(self, *args, **kwargs):
        super(CategoryAdmin, self).__init__(*args, **kwargs)
        self.prepopulated_fields = {'slug': ('title',)}
        self.fieldsets = (
            (None, {
                'fields': ('title', 'slug'),
            }),
            (_('Common Settings'), {
                'fields': ('parent',),
                'description': _(
                    'These fields are the same across all languages.'),
            }),
            (_('Date Information'), {
                'fields': ('date_created', 'last_modified'),
                'classes': ('collapse',),
                'description': _(
                    'These fields are the same across all languages.'),
            }),
        )


class TaggedPostInline(admin.TabularInline):
    model = TaggedPost
    extra = 0


class TagAdmin(admin.ModelAdmin):
    inlines = (TaggedPostInline,)


class PostAdmin(TranslatableAdmin, PlaceholderAdmin):
    list_display = (
        'title_', 'slug_', 'date_published',
        'author', 'all_translations', 'admin_image')
    list_filter = ('date_published', 'date_created', 'last_modified', 'author')
    readonly_fields = ('date_created', 'last_modified',)

    def __init__(self, *args, **kwargs):
        super(PostAdmin, self).__init__(*args, **kwargs)
        self.prepopulated_fields = {'slug': ('title',)}
        self.fieldsets = (
            (None, {
                'fields': ('title', 'slug', 'is_public'),
            }),
            (None, {
                'fields': ('subtitle', 'description', 'tags'),
            }),
            (_('Common Settings'), {
                'fields': (
                    'category', 'author', 'featured_image'),
                'description': _(
                    'These fields are the same across all languages.'),
            }),
            (_('Date Information'), {
                'fields': ('date_published', 'date_created', 'last_modified'),
                'classes': ('collapse',),
                'description': _(
                    'These fields are the same across all languages.'),
            }),
            (_('SEO Settings'), {
                'fields': ('meta_title', 'meta_description', 'meta_keywords'),
                'classes': ('collapse',)
            }),
            (None, {
                'fields': ('content',),
            }),
        )


admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
