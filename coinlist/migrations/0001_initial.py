# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-02 10:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coin_name', models.CharField(max_length=30)),
                ('coin_price', models.FloatField()),
                ('coin_img_url', models.URLField()),
                ('active_masternodes', models.IntegerField()),
                ('coins_daily', models.IntegerField()),
                ('collaterial', models.IntegerField(default=1000)),
            ],
        ),
    ]
