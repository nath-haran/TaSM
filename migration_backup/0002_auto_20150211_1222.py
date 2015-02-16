# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TaSM_site', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='productid',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='transaction',
            name='userid',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
    ]
