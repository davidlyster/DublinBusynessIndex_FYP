# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-06 17:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noiseLevels', '0004_reading_daterecorded'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reading',
            name='aleq',
            field=models.FloatField(default=0.0),
        ),
    ]
