# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('declaration', '0002_auto_20151126_0210'),
    ]

    operations = [
        migrations.AddField(
            model_name='declaration',
            name='nsfw',
            field=models.BooleanField(default=False),
        ),
    ]
