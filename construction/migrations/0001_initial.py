# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-23 17:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Alpha2_code', models.CharField(max_length=2)),
                ('Alpha3_code', models.CharField(max_length=100)),
            ],
        ),
    ]
