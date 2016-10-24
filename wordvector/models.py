from django.db import models
from pygments.lexers import get_lexer_by_name

class WordVector(models.Model):
  
    data_src = models.CharField(max_length=100)
    dimension = models.IntegerField(default=50)
    word_text = models.CharField(max_length=50)
    word_vector = models.CharField(max_length=10000) 
    
    class Meta:
        unique_together = ('data_src', 'dimension', 'word_text','word_vector')

    def save(self, *args, **kwargs):
        super(WordVector, self).save(*args, **kwargs)

        # limit the number of instances retained
        wordvectors = WordVector.objects.all()
        if len(wordvectors) > 100:
            wordvectors[0].delete()

class WordVectorFile(models.Model):
    data_src = models.CharField(max_length=100)
    dimension = models.IntegerField(default=50)
    doc = models.FileField(upload_to='doc/',default='doc/None/No-doc.zip')

    class Meta:
        unique_together = ('data_src', 'dimension','doc')

    def save(self, *args, **kwargs):
        super(WordVectorFile, self).save(*args, **kwargs)






