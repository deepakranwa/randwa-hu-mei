# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-13 11:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='thumb_pic',
            field=models.ImageField(blank=True, default=b'default_wli.jpeg', upload_to=b''),
        ),
    ]
