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

from blogit import utils


class Post(TranslatableModel):
    """
    Post model.
    """
    author = models.ForeignKey('Author', blank=True, null=True)
    featured_image = FilerImageField(blank=True, null=True)
    categories = models.ManyToManyField('Category', blank=True, null=True)
    is_public = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=datetime.now(), blank=True)
    last_modified = models.DateTimeField(default=datetime.now(), blank=True)

    translations = TranslatedFields(
        title = models.CharField(max_length=255),
        slug = models.SlugField(max_length=255),
        subtitle = models.CharField(max_length=255, blank=True, null=True),
        description = models.TextField(blank=True, null=True),
        tags = TaggableManager(blank=True),
    )

    content = PlaceholderField('blogit_post_content')

    class Meta:
        db_table = 'blogit_posts'

    @property
    def slug_(self):
        return self.get_slug()

    @property
    def title_(self):
        return self.__unicode__()

    def __unicode__(self):
        return self.lazy_translation_getter('title', '{}: {}'.format(_(u'Post'), self.pk))

    def get_slug(self, language=get_language()):
        return self.lazy_translation_getter('slug', '{}-{}'.format(_(u'post'), self.pk))

    def get_absolute_url(self, language=get_language()):
        return reverse('blogit_single', kwargs={'slug': self.get_slug(language=language)})

    def admin_image(self):
        return utils.thumb(self.featured_image, '72x72')
    admin_image.short_description = _(u'Featured image')
    admin_image.allow_tags = True


class Category(TranslatableModel):
    """
    Category model.
    """
    date_created = models.DateTimeField(default=datetime.now(), blank=True)
    last_modified = models.DateTimeField(default=datetime.now(), blank=True)

    translations = TranslatedFields(
        title = models.CharField(max_length=255),
        slug = models.SlugField(max_length=255),
    )

    class Meta:
        db_table = 'blogit_categories'
        verbose_name_plural = _(u'Categories')

    @property
    def slug_(self):
        return self.get_slug()

    @property
    def title_(self):
        return self.__unicode__()

    def __unicode__(self):
        return self.lazy_translation_getter('title', '{}: {}'.format(_(u'Category'), self.pk))

    def get_slug(self, language=get_language()):
        return self.lazy_translation_getter('slug', 'category-{}'.format(self.pk))

    def get_absolute_url(self, language=get_language()):
        return reverse('blogit_category', kwargs={'slug': self.get_slug(language=language)})


class Author(TranslatableModel):
    """
    Author model.
    """
    user = models.ForeignKey('auth.User', blank=True, null=True, unique=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    picture = FilerImageField(blank=True, null=True, related_name='author_image')

    translations = TranslatedFields(
        bio = models.TextField(blank=True, null=True),
    )

    class Meta:
        db_table = 'blogit_authors'

    def __unicode__(self):
        return self.name

    def get_absolute_url(self, language=get_language()):
        return reverse('blogit_author', kwargs={'slug': self.slug})

    def admin_image(self):
        return utils.thumb(self.picture, '72x72')
    admin_image.short_description = _(u'Author image')
    admin_image.allow_tags = True

