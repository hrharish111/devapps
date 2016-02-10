# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Created_form',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project_Name', models.CharField(max_length=100)),
                ('specification', models.CharField(max_length=100)),
                ('storage', models.CharField(max_length=100)),
                ('customer', models.CharField(max_length=100)),
                ('summary', models.CharField(max_length=100)),
                ('instance_type', models.CharField(max_length=100)),
                ('s3backet', models.CharField(max_length=100)),
                ('db_access', models.CharField(max_length=100)),
                ('stack', models.CharField(max_length=100)),
                ('server_access', models.CharField(max_length=100)),
            ],
        ),
    ]
