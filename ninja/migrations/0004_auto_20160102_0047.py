# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ninja', '0003_resultsource'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultsource',
            name='is_ninja',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
