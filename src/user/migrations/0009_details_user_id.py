# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-11-06 09:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20181106_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='user_id',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
