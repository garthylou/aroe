# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0005_make_filter_spec_unique'),
        ('wagtailcore', '0010_change_page_owner_to_null_on_delete'),
        ('aroe', '0007_simplepage_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='PressbookArticlePage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('text', wagtail.wagtailcore.fields.RichTextField(help_text='Text', verbose_name=b'Text', blank=True)),
                ('source', models.CharField(max_length=255, verbose_name='Source', blank=True)),
                ('detail', models.CharField(max_length=255, verbose_name='Source detail', blank=True)),
                ('icon_source', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name='icon', blank=True, to='wagtailimages.Image', null=True)),
                ('image', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name='image', blank=True, to='wagtailimages.Image', null=True)),
            ],
            options={
                'verbose_name': 'article for pressbook',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='PressbookPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'verbose_name': 'Pressbook page',
            },
            bases=('wagtailcore.page',),
        ),
    ]
