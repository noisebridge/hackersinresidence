# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-17 23:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_auto_20171221_0729'),
    ]

    operations = [
        migrations.AddField(
            model_name='opportunity',
            name='location_city',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='opportunity',
            name='location_country',
            field=models.TextField(null=True),
        ),
    ]
