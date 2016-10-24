from rest_framework import serializers
from wordvector.models import WordVector,WordVectorFile
from django.contrib.auth.models import User


class WordVectorSerializer(serializers.ModelSerializer):
	class Meta:
		model = WordVector
		fields = ('url', 'data_src', 'dimension', 'word_text', 'word_vector')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

class WordVectorFileSerializer(serializers.ModelSerializer):
	doc = serializers.FileField(max_length=None,use_url=True)
	class Meta:
		model = WordVectorFile
		fields = ('url','data_src','dimension','doc')


# class WordVector(models.Model):
#     data_src = models.CharField(max_length=100)
#     dimension = models.IntegerField(default=50)
#     word_text = models.CharField(max_length=50)
#     word_vector = models.CharField(max_length=10000)

#     class Meta:
#         unique_together = (('data_src', 'dimension', 'word_text'),)