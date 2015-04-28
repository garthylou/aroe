# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtaildocs', '0002_initial_data'),
        ('aroeapi', '0006_auto_20150313_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='training',
            name='document',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name='Documentation', blank=True, to='wagtaildocs.Document', null=True),
            preserve_default=True,
        ),
    ]
