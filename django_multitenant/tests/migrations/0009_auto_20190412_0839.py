# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-12 08:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_multitenant.fields


class Migration(migrations.Migration):

    dependencies = [
        ("tests", "0008_auto_20190412_0831"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="somerelatedmodel",
            name="opened",
        ),
        migrations.AddField(
            model_name="task",
            name="opened",
            field=models.BooleanField(default=True),
        ),
    ]
