# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-20 06:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construction', '0008_auto_20181020_1154'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('alpha2_code', models.CharField(blank=True, max_length=10)),
                ('alpha3_code', models.CharField(blank=True, max_length=10)),
            ],
        ),
    ]
