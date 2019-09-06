from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from musica.models import Musica
from musica.serializers import MusicaSerializer

# Create your views here.

class MusicaViewSets(viewsets.ModelViewSet):
    filter_backends = [SearchFilter]
    search_fields = ['^nome', '^artista','^genero_musica','^link']
    queryset = Musica.objects.all()
    serializer_class = MusicaSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)
