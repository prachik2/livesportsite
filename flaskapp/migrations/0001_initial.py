# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-10 04:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=20)),
                ('product_name', models.CharField(max_length=30)),
                ('order_status', models.CharField(max_length=20)),
                ('order_date', models.DateField()),
                ('order_deadline', models.DateField()),
                ('order_source', models.CharField(max_length=50)),
                ('product_code', models.CharField(max_length=30)),
                ('product_url', models.URLField()),
                ('customer_name', models.CharField(max_length=20)),
                ('selling_price', models.CharField(max_length=10)),
                ('quantity', models.CharField(max_length=20)),
                ('customer_email', models.CharField(max_length=30)),
                ('customer_phone', models.CharField(max_length=12)),
                ('customer_address', models.CharField(max_length=100)),
                ('payment_type', models.CharField(max_length=10)),
                ('procurement_status', models.CharField(max_length=40)),
                ('procurement_date', models.DateField()),
                ('supplier', models.CharField(max_length=50)),
                ('package_id', models.CharField(max_length=30)),
                ('consolidation_id', models.CharField(max_length=30)),
                ('usa_tracking', models.CharField(max_length=30)),
                ('tracking_number', models.CharField(max_length=30)),
                ('cost_price', models.CharField(max_length=10)),
                ('comments', models.CharField(max_length=50)),
                ('edit_log', models.CharField(max_length=20)),
            ],
        ),
    ]
