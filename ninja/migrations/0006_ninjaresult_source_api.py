# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ninja', '0005_ninjaresult_is_ninja'),
    ]

    operations = [
        migrations.AddField(
            model_name='ninjaresult',
            name='source_api',
            field=models.CharField(default='tmp', max_length=250),
            preserve_default=False,
        ),
    ]
