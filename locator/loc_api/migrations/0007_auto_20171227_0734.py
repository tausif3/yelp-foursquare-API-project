# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-27 07:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loc_api', '0006_auto_20171227_0714'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='locate_model_yelp',
            options={'verbose_name': 'database', 'verbose_name_plural': 'database'},
        ),
    ]
