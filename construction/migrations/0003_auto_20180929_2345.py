# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-29 18:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construction', '0002_auto_20180929_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='Phone_Number',
            field=models.IntegerField(blank=True),
        ),
    ]