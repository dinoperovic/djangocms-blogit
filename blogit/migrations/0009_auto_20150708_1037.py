# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogit', '0008_auto_20150708_0847'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='active',
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.IntegerField(default=0, help_text='When draft post is visible to staff only, when private to author only, and when public to everyone.', verbose_name='Status', choices=[(0, 'Draft'), (1, 'Private'), (2, 'Public'), (3, 'Hidden')]),
            preserve_default=True,
        ),
    ]
