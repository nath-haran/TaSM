# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TaSM_site', '0004_delete_transaction'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userid', models.CharField(max_length=200, db_column=b'userid')),
                ('productid', models.CharField(max_length=200, db_column=b'productid')),
                ('rating', models.IntegerField(default=0.0)),
                ('rating_time', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='transaction',
            unique_together=set([('userid', 'productid')]),
        ),
    ]
