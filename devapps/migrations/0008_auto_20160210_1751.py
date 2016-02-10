# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devapps', '0007_auto_20160210_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='created_form',
            name='specification',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='created_form',
            name='storage',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='created_form',
            name='summary',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='project_data',
            name='instance_id',
            field=models.CharField(max_length=100),
        ),
    ]
