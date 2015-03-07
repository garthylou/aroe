# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import aroeapi.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('family_name', models.CharField(max_length=200, verbose_name='Family name')),
                ('firstname', models.CharField(max_length=200, verbose_name='First name')),
                ('address', models.CharField(max_length=500, verbose_name='Address', blank=True)),
                ('zipcode', models.CharField(max_length=10, verbose_name='Zipcode', blank=True)),
                ('city', models.CharField(max_length=200, verbose_name='City', blank=True)),
                ('phone', models.CharField(max_length=100, verbose_name='Phone', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='Email', blank=True)),
                ('photo', models.ImageField(upload_to=aroeapi.models.path_members_photo, verbose_name='Photo', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
