# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True, help_text='Is this object active?', verbose_name='Active')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Date added')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Last modified')),
                ('posts', models.TextField()),
            ],
            options={
                'db_table': 'blogit_tags',
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TagTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language_code', models.CharField(max_length=15, verbose_name='Language', db_index=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('description', models.TextField(verbose_name='description', blank=True)),
                ('master', models.ForeignKey(related_name='translations', editable=False, to='blogit.Tag', null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'blogit_tags_translation',
                'db_tablespace': '',
                'default_permissions': (),
                'verbose_name': 'Tag Translation',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='tagtranslation',
            unique_together=set([('language_code', 'master'), ('slug', 'language_code')]),
        ),
    ]
