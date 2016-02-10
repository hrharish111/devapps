# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devapps', '0005_auto_20160210_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='created_form',
            name='storage',
            field=models.IntegerField(),
        ),
    ]
