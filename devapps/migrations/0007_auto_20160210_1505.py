# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devapps', '0006_auto_20160210_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='created_form',
            name='specification',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='created_form',
            name='summary',
            field=models.TextField(max_length=200),
        ),
    ]
