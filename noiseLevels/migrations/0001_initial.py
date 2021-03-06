# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-05 21:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Reading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=' ', max_length=100, null=True)),
                ('aleq', models.IntegerField(default=0)),
                ('dateTaken', models.DateTimeField(default=django.utils.timezone.now)),
                ('ruObj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='noiseLevels.Meter')),
            ],
        ),
    ]
