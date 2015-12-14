# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('declaration', '0003_declaration_nsfw'),
    ]

    operations = [
        migrations.AddField(
            model_name='declaration',
            name='ip_address',
            field=models.CharField(max_length=45, null=True, blank=True),
        ),
    ]
