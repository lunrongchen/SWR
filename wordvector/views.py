from rest_framework import permissions
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework import views
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from wordvector.models import WordVector
from wordvector.serializers import WordVectorSerializer,UserSerializer
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser,FileUploadParser,FormParser,MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import parser_classes
from rest_framework.decorators import api_view

class WordVectorViewSet(viewsets.ModelViewSet):
    queryset = WordVector.objects.all()
    serializer_class = WordVectorSerializer

    @detail_route(renderer_classes=(renderers.StaticHTMLRenderer,))

    def perform_create(self, serializer):
        serializer.save()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FileUploadView(views.APIView):
	parser_classes = (FileUploadParser,)

	def put(self,request,filename,format = None):
		file_obj = request.data['file']
		return Response(status = 204)
	