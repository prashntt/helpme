# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-20 11:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construction', '0009_nation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nation',
            name='Name',
            field=models.CharField(max_length=100),
        ),
    ]
