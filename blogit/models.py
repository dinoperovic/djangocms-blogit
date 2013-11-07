# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import get_language, ugettext_lazy as _
from hvad.models import TranslatableModel, TranslatedFields
from taggit.managers import TaggableManager
from cms.models.fields import PlaceholderField
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField

from datetime import datetime

from blogit import settings, utils


class Post(TranslatableModel):
    """
    Post model.
    """
    author = models.ForeignKey('Author', blank=True, null=True, verbose_name=_(u'Author'))
    featured_image = FilerImageField(blank=True, null=True, verbose_name=_(u'Featured image'))
    categories = models.ManyToManyField('Category', blank=True, null=True, verbose_name=_(u'Categories'))
    is_public = models.BooleanField(default=True, verbose_name=_(u'Is public'))
    date_created = models.DateTimeField(default=datetime.now(), verbose_name=_(u'Date created'))
    last_modified = models.DateTimeField(default=datetime.now(), verbose_name=_(u'Last modified'))

    translations = TranslatedFields(
        title = models.CharField(max_length=255, verbose_name=_(u'Title')),
        slug = models.SlugField(max_length=255, verbose_name=_(u'Slug')),
        subtitle = models.CharField(max_length=255, blank=True, null=True, verbose_name=_(u'Subtitle')),
        description = models.TextField(blank=True, null=True, verbose_name=_(u'Description')),
        tags = TaggableManager(blank=True, verbose_name=_(u'Tags')),
    )

    content = PlaceholderField('blogit_post_content', verbose_name=_(u'Content'))

    class Meta:
        db_table = 'blogit_posts'

    @property
    def slug_(self):
        return self.get_slug()

    @property
    def title_(self):
        return self.__unicode__()

    def save(self, *args, **kwargs):
        self.last_modified = datetime.now()
        super(Post, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.lazy_translation_getter('title', '{}: {}'.format(_(u'Post'), self.pk))

    def get_slug(self):
        return self.lazy_translation_getter('slug')

    def get_absolute_url(self):
        return reverse('blogit_single', kwargs={'post_slug': self.get_slug()})

    def get_tags(self):
        return self.lazy_translation_getter('tags')

    def admin_image(self):
        thumb = utils.thumb(self.featured_image, '72x72')
        return '<img src="{}">'.format(thumb) if thumb else _(u'(None)')
    admin_image.short_description = _(u'Featured image')
    admin_image.allow_tags = True


class Category(TranslatableModel):
    """
    Category model.
    """
    date_created = models.DateTimeField(default=datetime.now(), verbose_name=_(u'Date created'))
    last_modified = models.DateTimeField(default=datetime.now(), verbose_name=_(u'Last modified'))

    translations = TranslatedFields(
        title = models.CharField(max_length=255, verbose_name=_(u'Title')),
        slug = models.SlugField(max_length=255, verbose_name=_(u'Slug')),
    )

    class Meta:
        db_table = 'blogit_categories'
        verbose_name_plural = _(u'Categories')
        ordering = ('date_created',)

    @property
    def slug_(self):
        return self.get_slug()

    @property
    def title_(self):
        return self.__unicode__()

    def save(self, *args, **kwargs):
        self.last_modified = datetime.now()
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.lazy_translation_getter('title', '{}: {}'.format(_(u'Category'), self.pk))

    def get_slug(self):
        return self.lazy_translation_getter('slug')

    def get_absolute_url(self, language=None):
        if not language:
            language = get_language()

        return reverse('blogit_category', kwargs={
            'category_url': utils.get_translation('category', settings.BLOGIT_CATEGORY_URL_TRANSLATIONS, language),
            'category_slug': self.get_slug()
        })


class Author(TranslatableModel):
    """
    Author model.
    """
    user = models.ForeignKey('auth.User', blank=True, null=True, unique=True, verbose_name=_(u'User'))
    name = models.CharField(max_length=255, verbose_name=_(u'Name'))
    slug = models.SlugField(max_length=255, verbose_name=_(u'Slug'))
    picture = FilerImageField(blank=True, null=True, related_name='author_image', verbose_name=_(u'Picture'))

    translations = TranslatedFields(
        bio = models.TextField(blank=True, null=True, verbose_name=_(u'Bio')),
    )

    class Meta:
        db_table = 'blogit_authors'

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blogit_author', kwargs={'author_slug': self.slug})

    def admin_image(self):
        thumb = utils.thumb(self.picture, '72x72')
        return '<img src="{}">'.format(thumb) if thumb else _(u'(None)')
    admin_image.short_description = _(u'Author image')
    admin_image.allow_tags = True


class AuthorLink(models.Model):
    """
    Author link model.
    """
    author = models.ForeignKey('Author', related_name='author_links', verbose_name=_(u'Author'))
    link_type = models.CharField(max_length=255, choices=settings.BLOGIT_AUTHOR_LINK_TYPE_CHOICES,
        default=settings.BLOGIT_AUTHOR_LINK_TYPE_CHOICES[0][0], verbose_name=_(u'Link type'))

    url = models.CharField(max_length=255, verbose_name=_(u'Url'))

    class Meta:
        db_table = 'blogit_author_links'
        ordering = ('pk',)

    def __unicode__(self):
        return self.url
