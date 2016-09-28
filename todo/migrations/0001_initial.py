# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-23 02:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todoitem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_title', models.CharField(max_length=50)),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='CreatedTime')),
                ('isDone', models.BooleanField(default=False)),
            ],
        ),
    ]
