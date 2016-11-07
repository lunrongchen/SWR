from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from wordvector.models import WordVector, WordVectorFile
from wordvector.serializers import WordVectorSerializer, WordVectorFileSerializer
from rest_framework.parsers import JSONParser,FileUploadParser,FormParser,MultiPartParser
from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView

class WordvectorList(viewsets.ModelViewSet):
	queryset = WordVector.objects.all()
	serializer_class = WordVectorSerializer
	@detail_route(renderer_classes=(renderers.StaticHTMLRenderer,))
	def perform_create(self, serializer):
		instance = WordVectorFile.objects.get(data_src=serializer.validated_data['data_src'], dimension=serializer.validated_data['dimension'])
		serializer.save()
		instance.data_count = instance.data_count + 1;
		instance.save()

class WordvectorDetail(APIView):
	#def get_object(self, data_src, dimension, word_text):
	def get(self, request, data_src, dimension, word_text, format=None):
		try:
			wordvector = WordVector.objects.filter(data_src=data_src, dimension=dimension, word_text=word_text);
		except WordVector.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)
		serializer = WordVectorSerializer(wordvector, many=True)
		return Response(serializer.data)
	def delete(self, request, data_src, dimension, word_text, format=None):
	 	try:
			wordvector = WordVector.objects.filter(data_src=data_src, dimension=dimension, word_text=word_text);
		except WordVector.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)
	 	wordvector.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


class WordVectorFileList(viewsets.ModelViewSet):
	queryset = WordVectorFile.objects.all()
	serializer_class = WordVectorFileSerializer

	@detail_route(renderer_classes=(renderers.StaticHTMLRenderer,))
	def perform_create(self, serializer):
		serializer.save()

