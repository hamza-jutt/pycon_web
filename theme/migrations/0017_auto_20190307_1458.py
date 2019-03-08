# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-03-07 14:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0016_venue'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='is_video',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='gallery',
            name='video_link',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]