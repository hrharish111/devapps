# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devapps', '0008_auto_20160210_1751'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userdata',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_email', models.CharField(unique=True, max_length=100)),
                ('password', models.CharField(unique=True, max_length=100)),
            ],
        ),
    ]
