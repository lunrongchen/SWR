from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from wordvector.models import WordVector
from wordvector.serializers import WordVectorSerializer
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def wordvector_list(request, format=None):
	"""List all wordvectors, or create a new worvectors."""

	if request.method == 'GET':
		wordvectors = WordVector.objects.all();
		serializer = WordVectorSerializer(wordvectors, many=True);
		return Response(serializer.data);

	elif request.method == 'POST':
		serializer = WordVectorSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def wordvector_detail(request, data_src, dimension, word_text, format=None):
	"""
	Retrieve, update or delete a snippet instance.
	"""
	try:
		wordvectors = WordVector.objects.all();
		wordvector = wordvectors.filter(data_src=data_src)
		wordvector = wordvectors.filter(dimension=dimension)
		wordvector = wordvectors.filter(word_text=word_text)
	except WordVector.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = WordVectorSerializer(wordvector, many=True)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = WordVectorSerializer(wordvector, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		wordvector.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)