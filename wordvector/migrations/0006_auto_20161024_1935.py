# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordvector', '0005_auto_20161024_0117'),
    ]

    operations = [
        migrations.CreateModel(
            name='WordVectorFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_src', models.CharField(max_length=100)),
                ('dimension', models.IntegerField(default=50)),
                ('doc', models.FileField(default=b'doc/None/No-doc.zip', upload_to=b'doc/')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='wordvector',
            unique_together=set([('data_src', 'dimension', 'word_text', 'word_vector')]),
        ),
        migrations.AlterUniqueTogether(
            name='wordvectorfile',
            unique_together=set([('data_src', 'dimension', 'doc')]),
        ),
        migrations.RemoveField(
            model_name='wordvector',
            name='doc',
        ),
    ]
