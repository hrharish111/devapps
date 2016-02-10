# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('devapps', '0003_project_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_data',
            name='instance_type',
            field=models.CharField(default=datetime.datetime(2016, 2, 10, 13, 23, 7, 296258, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
