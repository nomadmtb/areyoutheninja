# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NinjaResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('test_date', models.DateTimeField(auto_now_add=True)),
                ('ip_address', models.CharField(max_length=200)),
                ('uuid', models.CharField(max_length=250)),
                ('image', models.CharField(max_length=200)),
                ('message', models.CharField(max_length=300)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
