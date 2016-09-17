# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-13 23:00
from __future__ import unicode_literals

from django.db import migrations
import game.models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0013_auto_20160913_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamestate',
            name='last_word_pos',
            field=game.models.ListField(default='[]', max_length=150),
        ),
        migrations.DeleteModel(
            name='WordLoc',
        ),
    ]