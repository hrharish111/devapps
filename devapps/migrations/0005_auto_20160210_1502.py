# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devapps', '0004_project_data_instance_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='created_form',
            name='project_Name',
            field=models.CharField(unique=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='created_form',
            name='storage',
            field=models.FloatField(),
        ),
    ]
