# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-20 19:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=1000)),
                ('weight', models.FloatField(max_length=45)),
                ('price', models.FloatField(max_length=45)),
                ('cost', models.FloatField(max_length=45)),
                ('category', models.CharField(max_length=255)),
            ],
        ),
    ]
