# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-21 12:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20161121_0829'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipologia',
            name='sugestao',
            field=models.TextField(null=True, unique=True),
        ),
    ]
