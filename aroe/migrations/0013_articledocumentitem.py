# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtaildocs', '0002_initial_data'),
        ('aroe', '0012_auto_20150331_1438'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleDocumentItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('caption', models.CharField(max_length=255, verbose_name='Title', blank=True)),
                ('document', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name='document', blank=True, to='wagtaildocs.Document', null=True)),
                ('page', modelcluster.fields.ParentalKey(related_name='document_items', to='aroe.ArticlePage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
