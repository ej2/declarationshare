# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Declaration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=4, choices=[(b'WILL', b'I will'), (b'AM', b'I am')])),
                ('date_created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True)),
                ('reminder_frequency', models.CharField(default=b'N', max_length=1)),
                ('user', models.ForeignKey(related_name='declarations', to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
