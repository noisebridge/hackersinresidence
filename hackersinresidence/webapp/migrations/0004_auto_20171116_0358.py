# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-16 03:58
from __future__ import unicode_literals

from django.db import migrations, models
import webapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20171115_0851'),
    ]

    operations = [
        migrations.AddField(
            model_name='opportunity',
            name='location',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='organization_banner',
            field=models.ImageField(default=None, upload_to=webapp.models.user_directory_path),
        ),
    ]