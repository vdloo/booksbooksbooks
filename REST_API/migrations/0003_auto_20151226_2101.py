# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-26 21:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('REST_API', '0002_auto_20151226_2022'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ('-year', 'author', 'title')},
        ),
        migrations.RemoveField(
            model_name='book',
            name='published',
        ),
        migrations.AddField(
            model_name='book',
            name='year',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
