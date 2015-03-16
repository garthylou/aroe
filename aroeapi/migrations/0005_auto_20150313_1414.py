# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aroeapi', '0004_training'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='end',
            field=models.DateTimeField(null=True, verbose_name='End', blank=True),
            preserve_default=True,
        ),
    ]
