# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-11-05 15:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20181105_2032'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User_details',
            new_name='user',
        ),
    ]