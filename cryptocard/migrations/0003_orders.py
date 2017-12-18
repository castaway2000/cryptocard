# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-17 21:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptocard', '0002_auto_20171217_0645'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=234)),
                ('description', models.CharField(max_length=234)),
                ('amount', models.CharField(max_length=4)),
                ('charge_id', models.CharField(max_length=234)),
            ],
        ),
    ]
