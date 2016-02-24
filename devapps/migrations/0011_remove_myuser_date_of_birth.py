# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devapps', '0010_auto_20160222_1300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='date_of_birth',
        ),
    ]
