# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-15 08:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('murder', '0004_auto_20180815_0759'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='enquete',
            unique_together=set([]),
        ),
    ]