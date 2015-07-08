# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogit', '0006_auto_20150707_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.IntegerField(default=0, verbose_name='Status', choices=[(0, 'Draft'), (1, 'Private'), (2, 'Public')]),
            preserve_default=True,
        ),
    ]
