# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-24 03:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20171123_1611'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='courseStudents',
        ),
        migrations.DeleteModel(
            name='News',
        ),
        migrations.DeleteModel(
            name='Schedule',
        ),
        migrations.RemoveField(
            model_name='task',
            name='taskStudents',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
