# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devapps', '0002_created_form_user_key'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project_data',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('instance_name', models.CharField(unique=True, max_length=100)),
                ('region', models.CharField(max_length=100)),
                ('instance_id', models.CharField(unique=True, max_length=100)),
                ('instance_ip', models.CharField(max_length=100)),
                ('instance_state', models.CharField(max_length=100)),
            ],
        ),
    ]
