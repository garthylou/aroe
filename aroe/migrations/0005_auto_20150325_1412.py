# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import wagtail.wagtailcore.fields
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0005_make_filter_spec_unique'),
        ('wagtailcore', '0010_change_page_owner_to_null_on_delete'),
        ('aroe', '0004_trainingpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleImageItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('caption', models.CharField(max_length=255, verbose_name='Title', blank=True)),
                ('image', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name='image', blank=True, to='wagtailimages.Image', null=True)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ArticlePage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('text_content', wagtail.wagtailcore.fields.RichTextField(help_text='Content of the article.', verbose_name=b'Content', blank=True)),
            ],
            options={
                'verbose_name': 'Article',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='DossierImageItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('caption', models.CharField(max_length=255, verbose_name='Title', blank=True)),
                ('image', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name='image', blank=True, to='wagtailimages.Image', null=True)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DossierPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('text_content', wagtail.wagtailcore.fields.RichTextField(help_text='Introduce the content of the Dossier.', verbose_name=b'Introduction', blank=True)),
            ],
            options={
                'verbose_name': 'Dossier',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AddField(
            model_name='dossierimageitem',
            name='page',
            field=modelcluster.fields.ParentalKey(related_name='image_items', to='aroe.DossierPage'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='articleimageitem',
            name='page',
            field=modelcluster.fields.ParentalKey(related_name='image_items', to='aroe.ArticlePage'),
            preserve_default=True,
        ),
    ]
