# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-20 06:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construction', '0007_worker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='Phone_Number',
            field=models.CharField(max_length=10),
        ),
    ]