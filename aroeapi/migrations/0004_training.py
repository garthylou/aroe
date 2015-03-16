# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aroeapi', '0003_auto_20150306_1147'),
    ]

    operations = [
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('start', models.DateTimeField(verbose_name='Start')),
                ('end', models.DateTimeField(verbose_name='End')),
                ('description', models.TextField(null=True, verbose_name='Description', blank=True)),
                ('responsible', models.CharField(max_length=200, null=True, verbose_name='Responsible', blank=True)),
                ('intervenant', models.CharField(max_length=250, null=True, verbose_name='Intervenant', blank=True)),
                ('seats', models.PositiveIntegerField(null=True, verbose_name='Seats', blank=True)),
                ('occupied_seats', models.PositiveIntegerField(null=True, verbose_name='Seats', blank=True)),
                ('location', models.CharField(max_length=300, null=True, verbose_name='Location', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
