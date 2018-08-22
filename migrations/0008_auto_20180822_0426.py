# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-22 04:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('murder', '0007_copie'),
    ]

    operations = [
        migrations.AddField(
            model_name='enquete',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='enquete',
            name='type',
            field=models.CharField(choices=[('E', 'ENQUETE'), ('I', 'INTERCEPTION'), ('C', 'COPIE')], default='E', max_length=1, verbose_name='Type'),
        ),
    ]
