# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-24 04:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20171124_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='newsDate',
            field=models.DateField(default=datetime.datetime(2017, 11, 24, 12, 1, 54, 489041)),
        ),
    ]
