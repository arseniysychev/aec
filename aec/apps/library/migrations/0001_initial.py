# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-25 09:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.PositiveSmallIntegerField(blank=True, choices=[(0, 'BLES level'), (1, 'GRAS level'), (2, 'GRAS level'), (3, 'GRAS level'), (4, 'GRAS level'), (5, 'GRAS level'), (6, 'GRAS level'), (7, 'HIGH level')], null=True)),
                ('lesson', models.PositiveSmallIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='library',
            unique_together=set([('level', 'lesson')]),
        ),
    ]
