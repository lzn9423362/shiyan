# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-19 05:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CookieApp', '0004_auto_20180918_0828'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='token',
            field=models.CharField(blank=True, default='', max_length=32, null=True),
        ),
    ]
