# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from hvad.admin import TranslatableAdmin
from cms.admin.placeholderadmin import PlaceholderAdmin

from blogit.models import Post, Category, Author, AuthorLink


class PostAdmin(TranslatableAdmin, PlaceholderAdmin):
    list_display = ('title_', 'slug_', 'date_created', 'last_modified', 'author', 'is_public', 'all_translations', 'admin_image')
    list_filter = ('date_created', 'last_modified', 'author', 'is_public')
    readonly_fields = ('last_modified',)

    def __init__(self, *args, **kwargs):
        super(PostAdmin, self).__init__(*args, **kwargs)
        self.prepopulated_fields = {'slug': ('title',)}
        self.fieldsets = (
            (None, {
                'fields': ['author', 'featured_image', 'categories', 'date_created', 'last_modified', 'is_public'],
            }),
            (_(u'Basic info'), {
                'fields': ['title', 'slug', 'subtitle', 'description', 'tags'],
            }),
            (_(u'Content'), {
                'fields': ['content'],
            }),
        )


class CategoryAdmin(TranslatableAdmin, PlaceholderAdmin):
    list_display = ('title_', 'slug_', 'date_created', 'last_modified', 'all_translations')
    list_filter = ('date_created', 'last_modified')
    readonly_fields = ('last_modified',)

    def __init__(self, *args, **kwargs):
        super(CategoryAdmin, self).__init__(*args, **kwargs)
        self.prepopulated_fields = {'slug': ('title',)}
        self.fieldsets = (
            (None, {
                'fields': ['date_created', 'last_modified'],
            }),
            (_(u'Basic info'), {
                'fields': ['title', 'slug'],
            }),
        )


class AuthorLinkInline(admin.StackedInline):
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
                'fields': ['user', 'name', 'slug', 'picture'],
            }),
            (_(u'Basic info'), {
                'fields': ['bio'],
            }),
        )


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
