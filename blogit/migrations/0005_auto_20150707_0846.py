# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def add_tags(apps, schema_editor):
    Post = apps.get_model('blogit', 'Post')
    Tag = apps.get_model('blogit', 'Tag')

    # post_pk: [tag_pk, tag_pk, ...]
    post_tags_map = {}
    for tag in Tag.objects.all():
        for pk in tag.posts.split(','):
            if pk:
                pk = int(pk)
                if pk not in post_tags_map:
                    post_tags_map[pk] = []
                post_tags_map[pk].append(tag.pk)

    for post_pk, tag_pks in post_tags_map.items():
        try:
            post = Post.objects.get(pk=post_pk)
            tags = Tag.objects.filter(pk__in=tag_pks)
            post.tags.add(*tags)
            post.save()
        except Post.DoesNotExist:
            pass


class Migration(migrations.Migration):

    dependencies = [
        ('blogit', '0004_auto_20150707_0845'),
    ]

    operations = [
        migrations.RunPython(add_tags),
    ]
