# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-19 01:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20190619_0006'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gamesreviews',
            old_name='is_top',
            new_name='isTop',
        ),
    ]