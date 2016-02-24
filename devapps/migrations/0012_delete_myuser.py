# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devapps', '0011_remove_myuser_date_of_birth'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MyUser',
        ),
    ]
