# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-10 05:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flaskapp', '0004_auto_20170910_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='consolidation_id',
            field=models.CharField(max_length=30, null=True),
        ),
    ]