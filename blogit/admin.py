# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from mptt.admin import MPTTModelAdmin
from hvad.admin import TranslatableAdmin
from cms.admin.placeholderadmin import PlaceholderAdmin

from .models import AuthorLink, Author, Category, Post


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
                    u'These fields are the same across all languages.'),
            }),
            (_(u'Personal Info'), {
                'fields': ('first_name', 'last_name', 'email', 'picture'),
                'description': _(
                    u'These fields are the same across all languages.'),
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
            (_(u'Common Settings'), {
                'fields': ('parent',),
                'description': _(
                    u'These fields are the same across all languages.'),
            }),
            (_(u'Date Information'), {
                'fields': ('date_created', 'last_modified'),
                'classes': ('collapse',),
                'description': _(
                    u'These fields are the same across all languages.'),
            }),
        )


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
            (_(u'Common Settings'), {
                'fields': (
                    'category', 'author', 'featured_image'),
                'description': _(
                    u'These fields are the same across all languages.'),
            }),
            (_(u'Date Information'), {
                'fields': ('date_published', 'date_created', 'last_modified'),
                'classes': ('collapse',),
                'description': _(
                    u'These fields are the same across all languages.'),
            }),
            (_(u'SEO Settings'), {
                'fields': ('meta_title', 'meta_description', 'meta_keywords'),
                'classes': ('collapse',)
            }),
            (_(u'Content'), {
                'fields': ('content',),
            }),
        )


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
