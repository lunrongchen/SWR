import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'SWR.settings'
from wordvector.models import WordVector
from wordvector.serializers import WordVectorSerializer

wordvector_tmp = WordVector(data_src='data_src2q1', dimension=200, word_text='northwestern', word_vector='123123')
# wordvector_tmp.save()

print(WordVector.objects.all())
# serializer = WordVectorSerializer(wordvector_tmp)
# serializer.data

# serializer = WordVectorSerializer(WordVector.objects.all(), many=True
# serializer.data