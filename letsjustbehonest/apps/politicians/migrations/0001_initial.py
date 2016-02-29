# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-29 01:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Politician',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=35)),
                ('last_name', models.CharField(max_length=35)),
                ('slug', models.CharField(max_length=50)),
                ('honesty_score', models.IntegerField(default=None, null=True)),
                ('party', models.CharField(max_length=20)),
                ('roles', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Statement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ruling', models.IntegerField(choices=[(0, 'True'), (1, 'Mostly True'), (2, 'Half True'), (3, 'Mostly False'), (4, 'False'), (5, 'Pants on Fire')], default=0)),
                ('ruling_headline', models.TextField()),
                ('quote', models.TextField()),
                ('context', models.TextField()),
                ('url', models.TextField()),
                ('statement_date', models.DateField(null=True)),
                ('ruling_datetime', models.DateTimeField(null=True)),
                ('speaker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='statements', to='politicians.Politician')),
            ],
        ),
    ]
