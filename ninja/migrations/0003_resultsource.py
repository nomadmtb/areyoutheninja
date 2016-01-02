# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ninja', '0002_auto_20151229_0629'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResultSource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('source_api', models.CharField(max_length=200)),
                ('result_message', models.CharField(max_length=500)),
                ('is_ninja', models.BooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
