# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-02 15:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coinlist', '0002_auto_20180502_1107'),
    ]

    operations = [
        migrations.AddField(
            model_name='coin',
            name='rpc_port',
            field=models.IntegerField(default=0),
        ),
    ]
