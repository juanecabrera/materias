# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 00:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20170404_0009'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estudiante',
            old_name='category',
            new_name='materia',
        ),
    ]
