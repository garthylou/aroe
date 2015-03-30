# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aroe', '0010_emptypage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emptypage',
            options={'verbose_name': 'Empty page'},
        ),
    ]
