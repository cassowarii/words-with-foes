# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-12 06:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0009_game_p1_turn'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='someone_moved',
            field=models.BooleanField(default=False, verbose_name='someone has moved'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='game',
            name='completed',
            field=models.BooleanField(verbose_name='completed'),
        ),
        migrations.AlterField(
            model_name='game',
            name='last_move',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 11, 23, 20, 4, 570639), verbose_name='last move'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='game',
            name='p1_turn',
            field=models.BooleanField(verbose_name="player 1's turn"),
        ),
        migrations.AlterField(
            model_name='game',
            name='p2_first',
            field=models.BooleanField(verbose_name='player 2 goes first'),
        ),
        migrations.AlterField(
            model_name='game',
            name='public',
            field=models.BooleanField(verbose_name='public'),
        ),
    ]
