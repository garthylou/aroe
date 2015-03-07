# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aroe', '0002_poste_member'),
    ]

    operations = [
        migrations.CreateModel(
            name='MembresPage',
            fields=[
                ('associationtilepage_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='aroe.AssociationTilePage')),
            ],
            options={
                'abstract': False,
            },
            bases=('aroe.associationtilepage',),
        ),
    ]
