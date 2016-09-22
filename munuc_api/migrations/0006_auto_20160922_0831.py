# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-22 08:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('munuc_api', '0005_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='committees',
        ),
        migrations.AddField(
            model_name='committee',
            name='countries',
            field=models.ManyToManyField(to='munuc_api.Country'),
        ),
    ]
