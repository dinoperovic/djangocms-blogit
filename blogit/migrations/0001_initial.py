# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image
import mptt.fields
import django.db.models.deletion
import cms.models.fields
import django.utils.timezone
from django.conf import settings
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('filer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(help_text='Text used in the url.', unique=True, max_length=100, verbose_name='slug')),
                ('first_name', models.CharField(max_length=30, null=True, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, null=True, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=75, null=True, verbose_name='email address', blank=True)),
                ('bio', cms.models.fields.PlaceholderField(slotname='blogit_author_bio', editable=False, to='cms.Placeholder', null=True)),
                ('picture', filer.fields.image.FilerImageField(related_name='author_image', verbose_name='picture', blank=True, to='filer.Image', null=True)),
                ('user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, blank=True, help_text='If selected, fields "First name", "Last name" and "Email address" will fallback tu "User" values if they are left empty.', unique=True, verbose_name='user')),
            ],
            options={
                'db_table': 'blogit_authors',
                'verbose_name': 'author',
                'verbose_name_plural': 'authors',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AuthorLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('link_type', models.CharField(max_length=255, null=True, verbose_name='type', blank=True)),
                ('url', models.URLField(verbose_name='url')),
                ('author', models.ForeignKey(related_name='links', verbose_name='author', to='blogit.Author')),
            ],
            options={
                'ordering': ('pk',),
                'db_table': 'blogit_author_links',
                'verbose_name': 'link',
                'verbose_name_plural': 'links',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AuthorTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(null=True, verbose_name='description', blank=True)),
                ('language_code', models.CharField(max_length=15, db_index=True)),
                ('master', models.ForeignKey(related_name='translations', editable=False, to='blogit.Author', null=True)),
            ],
            options={
                'abstract': False,
                'db_table': 'blogit_authors_translation',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date created')),
                ('last_modified', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last modified')),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', blank=True, to='blogit.Category', null=True)),
            ],
            options={
                'ordering': ('date_created',),
                'db_table': 'blogit_categories',
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CategoryTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('slug', models.SlugField(max_length=255, verbose_name='slug')),
                ('language_code', models.CharField(max_length=15, db_index=True)),
                ('master', models.ForeignKey(related_name='translations', editable=False, to='blogit.Category', null=True)),
            ],
            options={
                'abstract': False,
                'db_table': 'blogit_categories_translation',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='date created', blank=True)),
                ('last_modified', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last modified')),
                ('date_published', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='author', blank=True, to='blogit.Author', null=True)),
                ('category', mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='category', blank=True, to='blogit.Category', null=True)),
                ('content', cms.models.fields.PlaceholderField(slotname='blogit_post_content', editable=False, to='cms.Placeholder', null=True)),
                ('featured_image', filer.fields.image.FilerImageField(verbose_name='featured image', blank=True, to='filer.Image', null=True)),
            ],
            options={
                'ordering': ('-date_published',),
                'db_table': 'blogit_posts',
                'verbose_name': 'post',
                'verbose_name_plural': 'posts',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PostTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('slug', models.SlugField(help_text='Text used in the url.', max_length=255, verbose_name='slug')),
                ('is_public', models.BooleanField(default=True, help_text='Designates whether the post is visible to the public.', verbose_name='is public')),
                ('subtitle', models.CharField(max_length=255, null=True, verbose_name='subtitle', blank=True)),
                ('description', models.TextField(null=True, verbose_name='description', blank=True)),
                ('meta_title', models.CharField(help_text='Overwrites what is displayed at the top of your browser or in bookmarks.', max_length=255, null=True, verbose_name='page title', blank=True)),
                ('meta_description', models.TextField(help_text='A description of the page sometimes used by search engines.', null=True, verbose_name='description meta tag', blank=True)),
                ('meta_keywords', models.CharField(help_text='A list of comma separated keywords sometimes used by search engines.', max_length=255, null=True, verbose_name='keywords meta tag', blank=True)),
                ('language_code', models.CharField(max_length=15, db_index=True)),
                ('master', models.ForeignKey(related_name='translations', editable=False, to='blogit.Post', null=True)),
            ],
            options={
                'abstract': False,
                'db_table': 'blogit_posts_translation',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100, verbose_name='Name')),
                ('slug', models.SlugField(unique=True, max_length=100, verbose_name='Slug')),
            ],
            options={
                'ordering': ('name',),
                'db_table': 'blogit_tags',
                'verbose_name': 'tag',
                'verbose_name_plural': 'tags',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TaggedPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content_object', models.ForeignKey(verbose_name='post', to='blogit.PostTranslation')),
                ('tag', models.ForeignKey(related_name='tagged_posts', verbose_name='tag', to='blogit.Tag')),
            ],
            options={
                'db_table': 'blogit_tagged_post_translations',
                'verbose_name': 'tagged post',
                'verbose_name_plural': 'tagged posts',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='posttranslation',
            name='tags',
            field=taggit.managers.TaggableManager(to='blogit.Tag', through='blogit.TaggedPost', blank=True, help_text='A comma-separated list of tags.', verbose_name='tags'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='posttranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='categorytranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='authortranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
