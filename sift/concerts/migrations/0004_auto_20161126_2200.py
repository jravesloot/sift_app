# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-26 22:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concerts', '0003_artist_spotify_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]