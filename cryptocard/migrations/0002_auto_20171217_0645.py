# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-17 06:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cryptocard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactusmessage',
            name='user',
        ),
        migrations.DeleteModel(
            name='ContactUsMessage',
        ),
    ]
