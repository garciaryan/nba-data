# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_auto_20170926_2348'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.CharField(max_length=3, default=datetime.datetime(2017, 9, 27, 18, 59, 35, 302144, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
