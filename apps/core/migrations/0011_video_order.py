# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-03 11:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20180425_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='order',
            field=models.IntegerField(default=0, verbose_name='order'),
        ),
    ]
