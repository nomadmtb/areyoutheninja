# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ninja', '0004_auto_20160102_0047'),
    ]

    operations = [
        migrations.AddField(
            model_name='ninjaresult',
            name='is_ninja',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
