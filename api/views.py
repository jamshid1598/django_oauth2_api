from django.shortcuts import render
from rest_framework.generics import ListAPIView

from core.models import Library
from .serializers import LibrarySerializer

# Create your views here.

class LibraryAPIView(ListAPIView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer