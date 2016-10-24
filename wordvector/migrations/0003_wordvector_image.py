# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordvector', '0002_auto_20161021_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='wordvector',
            name='image',
            field=models.ImageField(default=b'Images/None/No-img.jpg', upload_to=b'Images/'),
        ),
    ]
