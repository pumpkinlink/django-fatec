# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculadora', '0002_auto_20170131_1159'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='logsoma',
            options={'verbose_name': 'Log de Soma'},
        ),
    ]
