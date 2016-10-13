# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WordVector',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_src', models.CharField(max_length=100)),
                ('dimension', models.IntegerField(default=50)),
                ('word_text', models.CharField(max_length=50)),
                ('word_vector', models.CharField(max_length=10000)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='wordvector',
            unique_together=set([('data_src', 'dimension', 'word_text')]),
        ),
    ]
