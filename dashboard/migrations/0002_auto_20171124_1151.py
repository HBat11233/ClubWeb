# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-24 03:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='newsDate',
            field=models.DateField(default=datetime.datetime(2017, 11, 24, 11, 50, 41, 811987)),
        ),
    ]
