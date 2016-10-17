# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-13 19:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0005_auto_20161003_1130'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpDownVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('object_pk', models.PositiveIntegerField()),
                ('vote', models.BooleanField(choices=[(True, 'Up Vote'), (False, 'Down Vote')], default=False)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
        migrations.RemoveField(
            model_name='message',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='question',
            name='down_votes',
        ),
        migrations.RemoveField(
            model_name='question',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='question',
            name='up_votes',
        ),
        migrations.AddField(
            model_name='message',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='modified'),
        ),
        migrations.AddField(
            model_name='question',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='modified'),
        ),
        migrations.AddField(
            model_name='video',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='modified'),
        ),
        migrations.AlterUniqueTogether(
            name='updownvote',
            unique_together=set([('user', 'object_pk', 'content_type')]),
        ),
    ]
