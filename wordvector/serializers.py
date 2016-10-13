from rest_framework import serializers
from wordvector.models import WordVector

class WordVectorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WordVector
        fields = ('url', 'data_src', 'dimension', 'word_text', 'word_vector')

# class WordVector(models.Model):
#     data_src = models.CharField(max_length=100)
#     dimension = models.IntegerField(default=50)
#     word_text = models.CharField(max_length=50)
#     word_vector = models.CharField(max_length=10000)

#     class Meta:
#         unique_together = (('data_src', 'dimension', 'word_text'),)