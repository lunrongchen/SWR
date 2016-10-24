# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordvector', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='wordvector',
            unique_together=set([('data_src', 'dimension', 'word_text', 'word_vector')]),
        ),
    ]
