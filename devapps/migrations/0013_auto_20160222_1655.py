# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('devapps', '0012_delete_myuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_data',
            name='application_url',
            field=models.URLField(default=datetime.datetime(2016, 2, 22, 16, 54, 40, 295895, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project_data',
            name='database_url',
            field=models.URLField(default=datetime.datetime(2016, 2, 22, 16, 54, 54, 432892, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project_data',
            name='testing_url',
            field=models.URLField(default=datetime.datetime(2016, 2, 22, 16, 55, 4, 541305, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
