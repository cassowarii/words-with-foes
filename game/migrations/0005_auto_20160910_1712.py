# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-11 00:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_gamestate_draw_pile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gamestate',
            old_name='p1letters',
            new_name='p1_letters',
        ),
        migrations.RenameField(
            model_name='gamestate',
            old_name='p2letters',
            new_name='p2_letters',
        ),
    ]
