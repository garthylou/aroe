# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0013_update_golive_expire_help_text'),
        ('aroeapi', '0007_training_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='training',
            name='page',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name='Documentations', blank=True, to='wagtailcore.Page', null=True),
            preserve_default=True,
        ),
    ]
