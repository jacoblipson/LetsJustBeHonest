# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-04 22:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('politicians', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='statement',
            name='ruling_datetime',
        ),
        migrations.AddField(
            model_name='statement',
            name='ruling_date',
            field=models.DateField(null=True),
        ),
        migrations.RemoveField(
            model_name='politician',
            name='roles',
        ),
        migrations.AddField(
            model_name='politician',
            name='roles',
            field=models.ManyToManyField(to='politicians.Role'),
        ),
    ]