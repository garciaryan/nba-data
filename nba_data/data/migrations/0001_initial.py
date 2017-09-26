# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('minutes', models.DecimalField(max_digits=3, decimal_places=1)),
                ('pts', models.DecimalField(max_digits=3, decimal_places=1)),
                ('fgm', models.DecimalField(max_digits=3, decimal_places=1)),
                ('fga', models.DecimalField(max_digits=3, decimal_places=1)),
                ('threes_m', models.DecimalField(max_digits=3, decimal_places=1)),
                ('threes_a', models.DecimalField(max_digits=3, decimal_places=1)),
                ('reb', models.DecimalField(max_digits=3, decimal_places=1)),
                ('ast', models.DecimalField(max_digits=3, decimal_places=1)),
                ('stl', models.DecimalField(max_digits=3, decimal_places=1)),
                ('blk', models.DecimalField(max_digits=3, decimal_places=1)),
                ('to', models.DecimalField(max_digits=3, decimal_places=1)),
            ],
        ),
    ]
