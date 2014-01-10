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
                    'author', 'featured_image', 'categories'),
                'description': _(
                    u'These fields are the same across all languages.'),
            }),
            (_(u'Content'), {
                'fields': ('content',),
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
                'fields': ('date_created', 'last_modified'),
            }),
            (_(u'Basic info'), {
                'fields': ('title', 'slug'),
            }),
        )


class AuthorLinkInline(admin.TabularInline):
    model = AuthorLink
    extra = 0


class AuthorAdmin(TranslatableAdmin, PlaceholderAdmin):
    list_display = ('name', 'slug', 'all_translations', 'admin_image')
    inlines = (AuthorLinkInline,)

    def __init__(self, *args, **kwargs):
        super(AuthorAdmin, self).__init__(*args, **kwargs)
        self.prepopulated_fields = {'slug': ('name',)}
        self.fieldsets = (
            (None, {
                'fields': ('user', 'name', 'slug', 'picture'),
            }),
            (_(u'Basic info'), {
                'fields': ('bio',),
            }),
        )


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
