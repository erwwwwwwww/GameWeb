# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-24 00:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='avater',
            field=models.ImageField(default='user/timg.jpg', upload_to='users', verbose_name='用户头像'),
        ),
    ]