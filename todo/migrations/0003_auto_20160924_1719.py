# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-24 09:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todoitem_deadline_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='deadline_time',
            field=models.DateTimeField(null=True, verbose_name='Deadline'),
        ),
    ]