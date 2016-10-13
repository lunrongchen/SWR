from wordvector.models import WordVector
from wordvector.serializers import WordVectorSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

wordvector_tmp = WordVector(data_src='data_src2', dimension=200, word_text='northwestern', word_vector='123123')
wordvector_tmp.save()

serializer = WordVectorSerializer(wordvector_tmp)
serializer.data


serializer = WordVectorSerializer(WordVector.objects.all(), many=True
serializer.data