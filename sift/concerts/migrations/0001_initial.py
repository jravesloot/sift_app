# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-20 00:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('re_string', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Concert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billing', models.CharField(max_length=200)),
                ('date_time', models.DateTimeField()),
                ('price', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=200)),
                ('date_scraped', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('artists', models.ManyToManyField(to='concerts.Artist')),
            ],
        ),
        migrations.CreateModel(
            name='ConcertMatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artists', models.ManyToManyField(to='concerts.Artist')),
                ('concert', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='concerts.Concert')),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('schedule_url', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='concert',
            name='venue',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='concerts.Venue'),
        ),
    ]
