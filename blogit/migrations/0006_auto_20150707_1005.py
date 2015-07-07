# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogit', '0005_auto_20150707_0846'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='posts',
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(related_name='tagged_posts', null=True, verbose_name='Tags', to='blogit.Tag', blank=True),
            preserve_default=True,
        ),
    ]
