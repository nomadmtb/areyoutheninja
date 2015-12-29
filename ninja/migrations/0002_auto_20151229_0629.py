# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ninja', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ninjaresult',
            name='uuid',
            field=models.CharField(unique=True, max_length=250),
            preserve_default=True,
        ),
    ]
