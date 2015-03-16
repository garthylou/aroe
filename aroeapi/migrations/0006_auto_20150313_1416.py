# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aroeapi', '0005_auto_20150313_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='end',
            field=models.DateField(null=True, verbose_name='End', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='training',
            name='start',
            field=models.DateField(verbose_name='Start'),
            preserve_default=True,
        ),
    ]
