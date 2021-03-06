# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-23 06:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20171116_0358'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='opportunity',
            options={'verbose_name_plural': 'Opportunities'},
        ),
        migrations.RemoveField(
            model_name='opportunity',
            name='location',
        ),
        migrations.AddField(
            model_name='organization',
            name='slug',
            field=models.SlugField(allow_unicode=True, default='nothin'),
            preserve_default=False,
        ),
    ]
