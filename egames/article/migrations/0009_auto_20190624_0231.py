# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-24 02:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_auto_20190624_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articleComments', to='article.Articles'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='avater',
            field=models.ImageField(default='users/defaultAvater.jpg', upload_to='users', verbose_name='用户头像'),
        ),
    ]
