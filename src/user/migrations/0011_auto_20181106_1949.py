# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-11-06 14:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_auto_20181106_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='details',
            name='user_id',
            field=models.CharField(max_length=20, null=True),
        ),
    ]