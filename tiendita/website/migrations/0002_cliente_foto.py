# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-30 19:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='foto',
            field=models.FileField(null=True, upload_to=b''),
        ),
    ]
