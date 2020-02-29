# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-02-28 06:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0003_auto_20200130_1000'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usematerial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usematerial_name', models.CharField(max_length=100)),
                ('quantity', models.PositiveIntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]