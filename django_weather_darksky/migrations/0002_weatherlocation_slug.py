# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-20 17:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_weather_darksky', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='weatherlocation',
            name='slug',
            field=models.SlugField(default=1, verbose_name='Slug'),
            preserve_default=False,
        ),
    ]