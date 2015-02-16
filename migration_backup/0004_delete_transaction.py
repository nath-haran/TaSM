# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TaSM_site', '0003_auto_20150211_1241'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Transaction',
        ),
    ]
