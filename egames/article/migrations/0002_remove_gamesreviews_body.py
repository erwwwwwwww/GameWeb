# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-09 14:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gamesreviews',
            name='body',
        ),
    ]
