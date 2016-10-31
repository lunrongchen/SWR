from rest_framework import serializers
from wordvector.models import WordVector, WordVectorFile
from django.contrib.auth.models import User

class WordVectorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WordVector
        fields = ('id', 'data_src', 'dimension', 'word_text', 'word_vector')

class WordVectorFileSerializer(serializers.ModelSerializer):
	data_link = serializers.FileField(max_length=None,use_url=True)
	class Meta:
		model = WordVectorFile
		fields = ('id', 'data_src', 'dimension', 'data_count', 'data_link')
