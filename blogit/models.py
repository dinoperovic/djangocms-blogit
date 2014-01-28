# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.utils.translation import get_language, ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

from mptt.models import MPTTModel, TreeForeignKey
from hvad.models import TranslatableModel, TranslatedFields
from taggit.managers import TaggableManager
from taggit.models import TagBase, ItemBase
from cms.models.fields import PlaceholderField
from filer.fields.image import FilerImageField

from blogit import settings as bs
from blogit.utils.translation import get_translation
from blogit.utils.noconflict import classmaker
from blogit.utils.image import thumb


# Author.
@python_2_unicode_compatible
class Author(TranslatableModel):
    user = models.ForeignKey(
        bs.AUTH_USER_MODEL, blank=True, null=True, unique=True,
        verbose_name=_('user'), help_text=_(
            'If selected, fields "First name", "Last name" and '
            '"Email address" will fallback tu "User" values if they are '
            'left empty.'))
    first_name = models.CharField(
        _('first name'), max_length=30, blank=True, null=True)
    last_name = models.CharField(
        _('last name'), max_length=30, blank=True, null=True)
    slug = models.SlugField(
        _('slug'), max_length=100, unique=True, help_text=_(
            'Text used in the url.'))
    email = models.EmailField(_('email address'), blank=True, null=True)
    picture = FilerImageField(
        blank=True, null=True, related_name='author_image',
        verbose_name=_('picture'))

    translations = TranslatedFields(
        description=models.TextField(_('description'), blank=True, null=True),
    )

    bio = PlaceholderField(
        'blogit_author_bio', verbose_name=_('bio'))

    class Meta:
        db_table = 'blogit_authors'
        verbose_name = _('author')
        verbose_name_plural = _('authors')

    def __str__(self):
        name = self.get_full_name()
        if not name and self.user and self.user.username:
            name = self.user.username
        return name or 'Author: {}'.format(self.pk)

    def get_absolute_url(self, language=None):
        if not language:
            language = get_language()

        return reverse('blogit_author_detail', kwargs={
            'url': get_translation(
                bs.AUTHOR_URL, bs.AUTHOR_URL_TRANSLATION, language),
            'slug': self.get_slug()
        })

    def get_slug(self):
        # If slug specified returns it, else returns pk.
        return self.slug if self.slug else self.pk

    def get_full_name(self):
        # Returns first_name plus last_name, with a space in between.
        name = '{} {}'.format(self.get_first_name(), self.get_last_name())
        return name.strip()

    def get_first_name(self):
        # Returns first_name, fallbacks to users first_name.
        if not self.first_name and self.user and self.user.first_name:
            return self.user.first_name
        return self.first_name or ''

    def get_last_name(self):
        # Returns last_name, fallbacks to users last_name.
        if not self.last_name and self.user and self.user.last_name:
            return self.user.last_name
        return self.last_name or ''

    def get_email(self):
        # Returns email, fallbacks to users email.
        if not self.email and self.user and self.user.email:
            return self.user.email
        return self.email or ''

    def get_posts(self):
        # Returns all posts by author.
        return Post.objects.language().filter(author=self, is_public=True)

    def admin_image(self):
        if self.picture:
            return '<img src="{}">'.format(
                thumb(self.picture, '72x72'))
        return None
    admin_image.short_description = _('author image')
    admin_image.allow_tags = True


@python_2_unicode_compatible
class AuthorLink(models.Model):
    author = models.ForeignKey(
        Author, related_name='author_links', verbose_name=_('author'))
    link_type = models.CharField(
        _('link type'), max_length=255, blank=True, null=True,
        choices=bs.AUTHOR_LINK_TYPE_CHOICES)
    url = models.URLField(_('url'))

    class Meta:
        db_table = 'blogit_author_links'
        verbose_name = _('author link')
        verbose_name_plural = _('author links')
        ordering = ('pk',)

    def __str__(self):
        return self.url


# Category.
@python_2_unicode_compatible
class Category(TranslatableModel, MPTTModel):
    __metaclass__ = classmaker()

    parent = TreeForeignKey(
        'self', blank=True, null=True, related_name='children', db_index=True)

    date_created = models.DateTimeField(
        _('date created'), default=timezone.now)
    last_modified = models.DateTimeField(
        _('last modified'), default=timezone.now)

    translations = TranslatedFields(
        title=models.CharField(_('title'), max_length=255),
        slug=models.SlugField(_('slug'), max_length=255),
        #description=models.TextField(
        #   _('description'), blank=True, null=True),
    )

    class Meta:
        db_table = 'blogit_categories'
        verbose_name = _('category')
        verbose_name_plural = _('categories')
        ordering = ('date_created',)

    class MPTTMeta:
        pass

    def __str__(self):
        return self.lazy_translation_getter(
            'title', '{}: {}'.format(_('Category'), self.pk))

    def save(self, *args, **kwargs):
        self.last_modified = timezone.now()
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self, language=None):
        if not language:
            language = get_language()

        return reverse('blogit_category_detail', kwargs={
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
        return self.__str__()


# Tag.
@python_2_unicode_compatible
class Tag(TagBase):
    class Meta:
        db_table = 'blogit_tags'
        verbose_name = _('tag')
        verbose_name_plural = _('tags')
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self, language=None):
        if not language:
            language = get_language()

        return reverse('blogit_tag_detail', kwargs={
            'url': get_translation(
                bs.TAG_URL, bs.TAG_URL_TRANSLATION, language),
            'slug': self.slug
        })


@python_2_unicode_compatible
class TaggedPost(ItemBase):
    tag = models.ForeignKey(
        Tag, related_name="tagged_posts", verbose_name=_('tag'))
    content_object = models.ForeignKey(
        'PostTranslation', verbose_name=_('post'))

    class Meta:
        db_table = 'blogit_tagged_post_translations'
        verbose_name = _('tagged post')
        verbose_name_plural = _('tagged posts')

    def __str__(self):
        return self.content_object.title

    @classmethod
    def tags_for(cls, model, instance=None):
        if instance is not None:
            return cls.tag_model().objects.filter(**{
                '%s__content_object' % cls.tag_relname(): instance
            })
        return cls.tag_model().objects.filter(**{
            '%s__content_object__isnull' % cls.tag_relname(): False
        }).distinct()


# Post.
@python_2_unicode_compatible
class Post(TranslatableModel):
    category = models.ForeignKey(
        Category, blank=True, null=True, on_delete=models.SET_NULL,
        verbose_name=_('category'))
    author = models.ForeignKey(
        Author, blank=True, null=True, on_delete=models.SET_NULL,
        verbose_name=_('author'))
    featured_image = FilerImageField(
        blank=True, null=True, verbose_name=_('featured image'))
    date_created = models.DateTimeField(
        _('date created'), blank=True, null=True, default=timezone.now)
    last_modified = models.DateTimeField(
        _('last modified'), default=timezone.now)
    date_published = models.DateTimeField(
        _('date published'), default=timezone.now)

    translations = TranslatedFields(
        title=models.CharField(_('title'), max_length=255),
        slug=models.SlugField(
            _('slug'), max_length=255,
            help_text=_('Text used in the url.')),
        is_public=models.BooleanField(
            _('is public'), default=True,
            help_text=_('Designates whether the post is visible to the '
                        'public.')),
        subtitle=models.CharField(
            _('subtitle'), max_length=255, blank=True, null=True),
        description=models.TextField(
            _('description'), blank=True, null=True),
        tags=TaggableManager(
            through=TaggedPost, blank=True, verbose_name=_('tags')),
        meta_title=models.CharField(
            _('page title'), max_length=255, blank=True, null=True,
            help_text=_('Overwrites what is displayed at the top of your '
                        'browser or in bookmarks.')),
        meta_description=models.TextField(
            _('description meta tag'), blank=True, null=True,
            help_text=_('A description of the page sometimes used by '
                        'search engines.')),
        meta_keywords=models.CharField(
            _('keywords meta tag'), max_length=255, blank=True, null=True,
            help_text=_('A list of comma separated keywords sometimes used '
                        'by search engines.')),
    )

    content = PlaceholderField(
        'blogit_post_content', verbose_name=_('content'))

    class Meta:
        db_table = 'blogit_posts'
        verbose_name = _('post')
        verbose_name_plural = _('posts')
        ordering = ('-date_published',)

    def __str__(self):
        return self.lazy_translation_getter(
            'title', '{}: {}'.format(_('Post'), self.pk))

    def save(self, *args, **kwargs):
        self.last_modified = timezone.now()
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        if bs.POST_DETAIL_URL_BY_DATE:
            return reverse('blogit_post_detail_by_date', kwargs={
                'year': self.date_published.strftime(bs.URL_YEAR_FORMAT),
                'month': self.date_published.strftime(
                    bs.URL_MONTH_FORMAT).lower(),
                'day': self.date_published.strftime(bs.URL_DAY_FORMAT),
                'slug': self.get_slug()
            })
        return reverse('blogit_post_detail', kwargs={'slug': self.get_slug()})

    def get_slug(self):
        return self.lazy_translation_getter('slug')

    def get_tags(self):
        return self.lazy_translation_getter('tags')

    def get_previous(self):
        # Returns previous post if it exists, if not returns None.
        posts = Post.objects.language().filter(
            date_published__lt=self.date_published).order_by('-date_published')
        return posts[0] if posts else None

    def get_next(self):
        # Returns next post if it exists, if not returns None.
        posts = Post.objects.language().filter(
            date_published__gt=self.date_published).order_by('date_published')
        return posts[0] if posts else None

    def admin_image(self):
        if self.featured_image:
            return '<img src="{}">'.format(
                thumb(self.featured_image, '72x72'))
        return None
    admin_image.short_description = _('featured image')
    admin_image.allow_tags = True

    @property
    def slug_(self):
        return self.get_slug()

    @property
    def title_(self):
        return self.__str__()


# Set PostTranslation unicode.
def post_translation_unicode(self):
    return self.title
PostTranslation.__unicode__ = post_translation_unicode  # noqa
PostTranslation.__str__ = post_translation_unicode  # noqa
