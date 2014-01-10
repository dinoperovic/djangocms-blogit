# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.utils.translation import get_language, ugettext_lazy as _

from hvad.models import TranslatableModel, TranslatedFields
from taggit.managers import TaggableManager
from cms.models.fields import PlaceholderField
from filer.fields.image import FilerImageField

from . import settings as bs
from .utils import get_translation, thumb


class Author(TranslatableModel):
    user = models.ForeignKey(
        bs.AUTH_USER_MODEL, blank=True, null=True, unique=True,
        verbose_name=_(u'user'))
    name = models.CharField(_(u'name'), max_length=255)
    slug = models.SlugField(_(u'slug'), max_length=255)
    picture = FilerImageField(
        blank=True, null=True, related_name='author_image',
        verbose_name=_(u'picture'))

    translations = TranslatedFields(
        bio=models.TextField(_(u'bio'), blank=True, null=True),
    )

    class Meta:
        db_table = 'blogit_authors'
        verbose_name = _(u'author')
        verbose_name_plural = _(u'authors')

    def __unicode__(self):
        return self.name

    def get_absolute_url(self, language=None):
        if not language:
            language = get_language()

        return reverse('blogit_author', kwargs={
            'url': get_translation(
                bs.AUTHOR_URL, bs.AUTHOR_URL_TRANSLATION, language),
            'slug': self.slug
        })

    def admin_image(self):
        if self.picture:
            return '<img src="{}">'.format(
                thumb(self.picture, '72x72'))
        return None
    admin_image.short_description = _(u'author image')
    admin_image.allow_tags = True


class AuthorLink(models.Model):
    author = models.ForeignKey(
        Author, related_name='author_links', verbose_name=_(u'author'))
    link_type = models.CharField(
        _(u'link type'), max_length=255, blank=True, null=True,
        choices=bs.AUTHOR_LINK_TYPE_CHOICES)
    url = models.URLField(_(u'url'))

    class Meta:
        db_table = 'blogit_author_links'
        verbose_name = _(u'author link')
        verbose_name_plural = _(u'author links')
        ordering = ('pk',)

    def __unicode__(self):
        return self.url


class Category(TranslatableModel):
    date_created = models.DateTimeField(
        _(u'date created'), default=timezone.now)
    last_modified = models.DateTimeField(
        _(u'last modified'), default=timezone.now)

    translations = TranslatedFields(
        title=models.CharField(_(u'title'), max_length=255),
        slug=models.SlugField(_(u'slug'), max_length=255),
    )

    class Meta:
        db_table = 'blogit_categories'
        verbose_name = _(u'category')
        verbose_name_plural = _(u'categories')
        ordering = ('date_created',)

    def __unicode__(self):
        return self.lazy_translation_getter(
            'title', '{}: {}'.format(_(u'Category'), self.pk))

    def save(self, *args, **kwargs):
        self.last_modified = timezone.now()
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self, language=None):
        if not language:
            language = get_language()

        return reverse('blogit_category', kwargs={
            'url': get_translation(
                bs.CATEGORY_URL, bs.CATEGORY_URL_TRANSLATION, language),
            'slug': self.get_slug()
        })

    def get_slug(self):
        return self.lazy_translation_getter('slug')

    @property
    def slug_(self):
        return self.get_slug()

    @property
    def title_(self):
        return self.__unicode__()


class Post(TranslatableModel):
    author = models.ForeignKey(
        Author, blank=True, null=True, verbose_name=_(u'author'))
    featured_image = FilerImageField(
        blank=True, null=True, verbose_name=_(u'featured image'))
    categories = models.ManyToManyField(
        Category, blank=True, null=True, verbose_name=_(u'categories'))
    date_created = models.DateTimeField(
        _(u'date created'), blank=True, null=True, default=timezone.now)
    last_modified = models.DateTimeField(
        _(u'last modified'), default=timezone.now)
    date_published = models.DateTimeField(
        _(u'date published'), default=timezone.now)

    translations = TranslatedFields(
        title=models.CharField(_(u'title'), max_length=255),
        slug=models.SlugField(
            _(u'slug'), max_length=255,
            help_text=_(u'Text used in the url.')),
        is_public=models.BooleanField(
            _(u'is public'), default=True, help_text=_(
                u'Designates whether the post is visible to the public.')),
        subtitle=models.CharField(
            _(u'subtitle'), max_length=255, blank=True, null=True),
        description=models.TextField(
            _(u'description'), blank=True, null=True),
        tags=TaggableManager(blank=True, verbose_name=_(u'tags')),
    )

    content = PlaceholderField(
        'blogit_post_content', verbose_name=_(u'content'))

    class Meta:
        db_table = 'blogit_posts'
        verbose_name = _(u'post')
        verbose_name_plural = _(u'posts')
        ordering = ('-date_published',)

    def __unicode__(self):
        return self.lazy_translation_getter(
            'title', '{}: {}'.format(_(u'Post'), self.pk))

    def save(self, *args, **kwargs):
        self.last_modified = timezone.now()
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blogit_detail', kwargs={'slug': self.get_slug()})

    def get_slug(self):
        return self.lazy_translation_getter('slug')

    def get_tags(self):
        return self.lazy_translation_getter('tags')

    def admin_image(self):
        if self.featured_image:
            return '<img src="{}">'.format(
                thumb(self.featured_image, '72x72'))
        return None
    admin_image.short_description = _(u'featured image')
    admin_image.allow_tags = True

    @property
    def slug_(self):
        return self.get_slug()

    @property
    def title_(self):
        return self.__unicode__()
