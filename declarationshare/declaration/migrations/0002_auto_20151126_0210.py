# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('declaration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='declaration',
            name='anonymous',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='declaration',
            name='author',
            field=models.CharField(max_length=b'50', null=True),
        ),
    ]
