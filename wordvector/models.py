import zipfile
import re
import django
import os
from django.db import models
from pygments.lexers import get_lexer_by_name
from shutil import rmtree

class WordVector(models.Model):
    data_src = models.CharField(max_length=100)
    dimension = models.IntegerField(default=50)
    word_text = models.CharField(max_length=50)
    word_vector = models.CharField(max_length=10000)

    class Meta:
        unique_together = (('data_src', 'dimension', 'word_text'),)

    def save(self, *args, **kwargs):
        super(WordVector, self).save(*args, **kwargs)

        # limit the number of instances retained
        wordvectors = WordVector.objects.all()
        if len(wordvectors) > 100:
            wordvectors[0].delete()

class WordVectorFile(models.Model):
    data_src = models.CharField(max_length=100)
    dimension = models.IntegerField(default=50)
    data_count = models.IntegerField(default=0)
    data_link = models.FileField(upload_to='data_link/',default='data_link/None/No-data_link.zip')

    class Meta:
        unique_together = (('data_src', 'dimension'),)

    def save(self, *args, **kwargs):
        super(WordVectorFile, self).save(*args, **kwargs)
        wordvectorfiles = WordVectorFile.objects.all()

    def get_data_src(model):
        return model._meta.data_src

    def get_dimension(model):
        return model._meta.dimension

    def get_data_count(model):
        return model._meta.data_count

    def get_data_link(model):
        return model._meta.data_link
