# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 00:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=b'No title', max_length=50)),
                ('photo', models.ImageField(upload_to=b'photos/')),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('favorite', models.BooleanField(default=False)),
                ('comment', models.CharField(blank=True, max_length=200)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.Category')),
            ],
        ),
    ]
