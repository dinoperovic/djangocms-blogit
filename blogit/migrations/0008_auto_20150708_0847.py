# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogit', '0007_post_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='posttranslation',
            name='meta_description',
            field=models.TextField(help_text='The text displayed in search engines.', max_length=155, verbose_name='Meta description', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='posttranslation',
            name='meta_title',
            field=models.CharField(max_length=255, verbose_name='Meta title', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.IntegerField(default=0, help_text='When draft post is visible to staff only, when private to author only, and when public to everyone.', verbose_name='Status', choices=[(0, 'Draft'), (1, 'Private'), (2, 'Public')]),
            preserve_default=True,
        ),
    ]
