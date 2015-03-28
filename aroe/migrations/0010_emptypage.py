# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('aroe', '0009_auto_20150327_1156'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmptyPage',
            fields=[
                ('associationtilepage_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='aroe.AssociationTilePage')),
                ('text', wagtail.wagtailcore.fields.RichTextField(help_text='Text', verbose_name=b'Text')),
            ],
            options={
                'abstract': False,
            },
            bases=('aroe.associationtilepage',),
        ),
    ]
