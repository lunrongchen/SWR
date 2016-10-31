# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordvector', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WordVectorFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_src', models.CharField(max_length=100)),
                ('dimension', models.IntegerField(default=50)),
                ('data_count', models.IntegerField(default=0)),
                ('data_link', models.FileField(default=b'data_link/None/No-data_link.zip', upload_to=b'data_link/')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='wordvectorfile',
            unique_together=set([('data_src', 'dimension')]),
        ),
    ]
