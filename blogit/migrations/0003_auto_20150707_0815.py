# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


def create_tags(apps, schema_editor):
    Tag = apps.get_model('blogit', 'Tag')
    TagTranslation = apps.get_model('blogit', 'TagTranslation')

    TaggitTag = apps.get_model('taggit', 'Tag')

    for tag in TaggitTag.objects.all():
        post_pks = [str(x) for x in tag.taggit_taggeditem_items.values_list(
            'object_id', flat=True)]
        t = Tag(posts=','.join(post_pks))
        t.save()

        for lang in settings.LANGUAGES:
            TagTranslation(
                master=t, language_code=lang[0],
                name=tag.name, slug=tag.slug,
            ).save()


class Migration(migrations.Migration):

    dependencies = [
        ('blogit', '0002_auto_20150707_0815'),
    ]

    operations = [
        migrations.RunPython(create_tags),
    ]
