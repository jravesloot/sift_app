# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-22 15:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concerts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concert',
            name='billing',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='concert',
            name='url',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='venue',
            name='address',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='venue',
            name='schedule_url',
            field=models.CharField(max_length=300),
        ),
    ]
