# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from hvad.admin import TranslatableAdmin
from cms.admin.placeholderadmin import PlaceholderAdmin

from .models import Post, Category, Author, AuthorLink


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


class CategoryAdmin(TranslatableAdmin, PlaceholderAdmin):
    list_display = (
        'title_', 'slug_', 'date_created', 'last_modified', 'all_translations')
    list_filter = ('date_created', 'last_modified')
    readonly_fields = ('last_modified',)

    def __init__(self, *args, **kwargs):
        super(CategoryAdmin, self).__init__(*args, **kwargs)
        self.prepopulated_fields = {'slug': ('title',)}
        self.fieldsets = (
            (None, {
                'fields': ('title', 'slug'),
            }),
            (_(u'Date Information'), {
                'fields': ('date_created', 'last_modified'),
                'classes': ('collapse',),
                'description': _(
                    u'These fields are the same across all languages.'),
            }),
        )


class AuthorLinkInline(admin.TabularInline):
    model = AuthorLink
    extra = 0


class AuthorAdmin(TranslatableAdmin, PlaceholderAdmin):
    list_display = ('__unicode__', 'slug', 'all_translations', 'admin_image')
    inlines = (AuthorLinkInline,)

    def __init__(self, *args, **kwargs):
        super(AuthorAdmin, self).__init__(*args, **kwargs)
        self.prepopulated_fields = {'slug': ('first_name', 'last_name')}
        self.fieldsets = (
            (None, {
                'fields': ('bio',),
            }),
            (_(u'Common Settings'), {
                'fields': (
                    'user', 'first_name', 'last_name', 'slug', 'email',
                    'picture'),
                'description': _(
                    u'These fields are the same across all languages.'),
            }),
        )


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
