# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import aroeapi.models


class Migration(migrations.Migration):

    dependencies = [
        ('aroeapi', '0002_auto_20150306_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='photo',
            field=models.ImageField(upload_to=aroeapi.models.path_members_photo, null=True, verbose_name='Photo', blank=True),
            preserve_default=True,
        ),
    ]
