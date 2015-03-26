# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('aroe', '0006_simplepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='simplepage',
            name='text',
            field=wagtail.wagtailcore.fields.RichTextField(help_text='Text', verbose_name=b'Text', blank=True),
            preserve_default=True,
        ),
    ]
