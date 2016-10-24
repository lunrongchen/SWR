# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordvector', '0003_wordvector_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='wordvector',
            name='doc',
            field=models.FileField(default=b'doc/None/No-doc.zip', upload_to=b'doc/'),
        ),
        migrations.AlterField(
            model_name='wordvector',
            name='image',
            field=models.ImageField(default=b'image/None/No-img.jpg', upload_to=b'image/'),
        ),
        migrations.AlterUniqueTogether(
            name='wordvector',
            unique_together=set([('data_src', 'dimension', 'word_text', 'word_vector', 'image', 'doc')]),
        ),
    ]
