from rest_framework import serializers
from wordvector.models import WordVector, WordVectorFile
from django.contrib.auth.models import User

class WordVectorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WordVector
        fields = ('url', 'data_src', 'dimension', 'word_text', 'word_vector')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

class WordVectorFileSerializer(serializers.ModelSerializer):
	class Meta:
		model = WordVectorFile
		fields = ('url', 'data_src', 'dimension', 'data_count', 'data_link')
