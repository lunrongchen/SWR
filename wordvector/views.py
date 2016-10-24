from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from wordvector.models import WordVector
from wordvector.serializers import WordVectorSerializer
from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView

class WordvectorList(APIView):
	def get(self, request, format=None):
		wordvectors = WordVector.objects.all();
		serializer = WordVectorSerializer(wordvectors, many=True);
		return Response(serializer.data);
	def post(self, request, format=None):
		serializer = WordVectorSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WordvectorDetail(APIView):
	#def get_object(self, data_src, dimension, word_text):
	 	
	def get(self, request, data_src, dimension, word_text, format=None):
		try:
			wordvector = WordVector.objects.filter(data_src=data_src, dimension=dimension, word_text=word_text);
		except WordVector.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)
		serializer = WordVectorSerializer(wordvector, many=True)
		return Response(serializer.data)
	def put(self, request, data_src, dimension, word_text, format=None):
		try:
			wordvector = WordVector.objects.filter(data_src=data_src, dimension=dimension, word_text=word_text);
		except WordVector.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)
		serializer = WordVectorSerializer(wordvector, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	def delete(self, request, data_src, dimension, word_text, format=None):
	 	try:
			wordvector = WordVector.objects.filter(data_src=data_src, dimension=dimension, word_text=word_text);
		except WordVector.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)
	 	wordvector.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)