# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aroe', '0011_auto_20150330_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pressbookarticlepage',
            name='source',
            field=models.CharField(help_text='Name of the source', max_length=255, verbose_name='Source'),
            preserve_default=True,
        ),
    ]
