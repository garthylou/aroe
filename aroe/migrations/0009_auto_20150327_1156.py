# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('aroe', '0008_pressbookarticlepage_pressbookpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pressbookarticlepage',
            name='detail',
            field=models.CharField(help_text='Detail of the source (publication date, # of the mag, ...)', max_length=255, verbose_name='Source detail'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pressbookarticlepage',
            name='icon_source',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name='icon', to='wagtailimages.Image', help_text='Icon of the source to display in pressbook.', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pressbookarticlepage',
            name='source',
            field=models.CharField(help_text='Title of the source', max_length=255, verbose_name='Source'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pressbookarticlepage',
            name='text',
            field=wagtail.wagtailcore.fields.RichTextField(help_text='Text', verbose_name=b'Text'),
            preserve_default=True,
        ),
    ]
