# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-13 03:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0010_auto_20160911_2320'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamestate',
            name='last_word',
            field=models.CharField(default='', max_length=15),
            preserve_default=False,
        ),
    ]
