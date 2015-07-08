# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models import Q
from django.core.urlresolvers import reverse
from django.conf import settings
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

from mptt.models import MPTTModel, TreeForeignKey
from parler.models import TranslatableModel, TranslatedFields
from parler.managers import TranslatableManager, TranslatableQuerySet
from cms.models.fields import PlaceholderField
from filer.fields.image import FilerImageField

from blogit import settings as bs

USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


@python_2_unicode_compatible
class Category(MPTTModel, TranslatableModel):
    """
    Category
    """
    active = models.BooleanField(
        _('Active'), default=True, help_text=bs.ACTIVE_FIELD_HELP_TEXT)
    date_added = models.DateTimeField(_('Date added'), auto_now_add=True)
    last_modified = models.DateTimeField(_('Last modified'), auto_now=True)

    parent = TreeForeignKey(
        'self', blank=True, null=True,
        related_name='children', verbose_name=_('Parent'))

    translations = TranslatedFields(
        name=models.CharField(_('Name'), max_length=255),
        slug=models.SlugField(_('Slug'), db_index=True),
        description=models.TextField(_('description'), blank=True),
        meta={'unique_together': [('slug', 'language_code')]},
    )

    objects = TranslatableManager()

    class Meta:
        db_table = 'blogit_categories'
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.safe_translation_getter('name')

    def get_absolute_url(self):
        return reverse('blogit_category_detail', kwargs={
            'slug': self.safe_translation_getter('slug')})


class Tag(TranslatableModel):
    """
    Tag
    """
    active = models.BooleanField(
        _('Active'), default=True, help_text=bs.ACTIVE_FIELD_HELP_TEXT)
    date_added = models.DateTimeField(_('Date added'), auto_now_add=True)
    last_modified = models.DateTimeField(_('Last modified'), auto_now=True)

    translations = TranslatedFields(
        name=models.CharField(_('Name'), max_length=255),
        slug=models.SlugField(_('Slug'), db_index=True),
        description=models.TextField(_('description'), blank=True),
        meta={'unique_together': [('slug', 'language_code')]},
    )

    objects = TranslatableManager()

    class Meta:
        db_table = 'blogit_tags'
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')

    def __str__(self):
        return self.safe_translation_getter('name')


class PostQuerySet(TranslatableQuerySet):
    def published(self, **kwargs):
        return self.filter(date_published__lte=timezone.now, **kwargs)


class PostManager(TranslatableManager):
    queryset_class = PostQuerySet

    def published(self, request, **kwargs):
        statuses = [Post.PUBLIC]
        if request.user and request.user.is_staff:
            statuses.append(Post.DRAFT)

        queryset = self.get_queryset().published(
            status__in=statuses, active=True, **kwargs)

        if request.user.is_authenticated():
            queryset = queryset | self.private(request.user, **kwargs)
        return queryset

    def draft(self, **kwargs):
        return self.get_queryset().filter(
            status=Post.DRAFT, active=True, **kwargs)

    def private(self, user, **kwargs):
        return self.get_queryset().filter(
            status=Post.PRIVATE, author=user, active=True, **kwargs)

    def public(self, **kwargs):
        return self.get_queryset().filter(
            status=Post.PUBLIC, active=True, **kwargs)


@python_2_unicode_compatible
class Post(TranslatableModel):
    """
    Post
    """
    DRAFT = 0  # Post is visible to staff
    PRIVATE = 1  # Post is visible to author only
    PUBLIC = 2  # Post is public given that date_published has passed

    STATUS_CODES = (
        (DRAFT, _('Draft')),
        (PRIVATE, _('Private')),
        (PUBLIC, _('Public')),
    )

    active = models.BooleanField(
        _('Active'), default=True, help_text=bs.ACTIVE_FIELD_HELP_TEXT)
    date_added = models.DateTimeField(_('Date added'), auto_now_add=True)
    last_modified = models.DateTimeField(_('Last modified'), auto_now=True)

    status = models.IntegerField(
        _('Status'), choices=STATUS_CODES, default=DRAFT,
        help_text=_('When draft post is visible to staff only, when private '
                    'to author only, and when public to everyone.'))

    date_published = models.DateTimeField(
        _('Published On'), default=timezone.now)

    category = TreeForeignKey(
        Category, blank=True, null=True, on_delete=models.SET_NULL,
        verbose_name=_('Category'))

    author = models.ForeignKey(
        USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
        verbose_name=_('Author'))

    featured_image = FilerImageField(
        blank=True, null=True, verbose_name=_('Featured Image'))

    translations = TranslatedFields(
        title=models.CharField(_('Title'), max_length=255),
        slug=models.SlugField(_('Slug'), db_index=True),
        description=models.TextField(_('Description'), blank=True),
        meta={'unique_together': [('slug', 'language_code')]},
    )

    body = PlaceholderField('blogit_post_body', related_name='post_body_set')

    tags = models.ManyToManyField(
        Tag, blank=True, null=True,
        related_name='tagged_posts', verbose_name=_('Tags'))

    objects = PostManager()

    class Meta:
        db_table = 'blogit_posts'
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')
        ordering = ('-date_published', '-date_added')
        get_latest_by = 'date_published'

    def __str__(self):
        return self.safe_translation_getter('title')

    def get_absolute_url(self):
        if bs.POST_DETAIL_DATE_URL:
            return reverse('blogit_post_detail_date', kwargs={
                'year': self.date_published.year,
                'month': self.date_published.month,
                'day': self.date_published.day,
                'slug': self.safe_translation_getter('slug'),
            })

        return reverse('blogit_post_detail', kwargs={
            'slug': self.safe_translation_getter('slug')})

    @property
    def name(self):
        return self.safe_translation_getter('title')
