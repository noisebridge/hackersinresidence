# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-18 04:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_auto_20180218_0352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opportunity',
            name='location_city',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='location_country',
            field=models.TextField(blank=True, null=True),
        ),
    ]
