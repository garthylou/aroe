# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aroeapi', '0003_auto_20150306_1147'),
        ('aroe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='poste',
            name='member',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name='Member', blank=True, to='aroeapi.Member', null=True),
            preserve_default=True,
        ),
    ]
