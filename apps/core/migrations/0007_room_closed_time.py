# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-18 11:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_room_external_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='closed_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='closed time'),
        ),
    ]
