# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-29 18:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construction', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Phone_Number', models.IntegerField(blank=True, max_length=10)),
                ('Email', models.EmailField(max_length=254)),
                ('Message', models.TextField(max_length=250)),
            ],
        ),
        migrations.DeleteModel(
            name='country',
        ),
    ]
