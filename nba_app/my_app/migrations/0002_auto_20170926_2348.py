# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='ast',
            new_name='assists',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='blk',
            new_name='blocks',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='pts',
            new_name='points',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='reb',
            new_name='rebounds',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='stl',
            new_name='steals',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='to',
            new_name='turnovers',
        ),
    ]
