# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('TaSM_site', '0010_auto_20150213_1356'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('productid', models.CharField(max_length=200, serialize=False, primary_key=True)),
                ('product_name', models.CharField(max_length=200)),
                ('product_price', models.CharField(default=0.0, max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('userid', models.CharField(max_length=200, serialize=False, primary_key=True)),
                ('username', models.CharField(default=b'user', max_length=200)),
                ('email', models.EmailField(default=b'nath.haran@gmail.com', max_length=75, verbose_name=b'email address')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
