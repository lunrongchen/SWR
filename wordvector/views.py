from rest_framework import permissions
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from wordvector.models import WordVector
from wordvector.serializers import WordVectorSerializer
from wordvector.serializers import UserSerializer
from django.contrib.auth.models import User

class WordVectorViewSet(viewsets.ModelViewSet):
    queryset = WordVector.objects.all()
    serializer_class = WordVectorSerializer

    @detail_route(renderer_classes=(renderers.StaticHTMLRenderer,))

    def perform_create(self, serializer):
        serializer.save()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer