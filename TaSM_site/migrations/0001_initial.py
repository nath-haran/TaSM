# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
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
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.IntegerField(default=0.0)),
                ('rating_time', models.DateTimeField()),
                ('productid', models.ForeignKey(to='TaSM_site.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userid', models.CharField(max_length=200, serialize=False, primary_key=True)),
                ('username', models.CharField(default=b'user', max_length=200)),
                ('password', models.CharField(default=b'password', max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='transaction',
            name='userid',
            field=models.ForeignKey(to='TaSM_site.User'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='transaction',
            unique_together=set([('userid', 'productid')]),
        ),
    ]
