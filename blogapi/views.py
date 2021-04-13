from django.shortcuts import render
from rest_framework import (
    generics, 
    permissions,
)
from .permissions import IsAutherOrReadOnly
# Create your views here.


from .models import Blog
from api.serializers import BlogSerializer


class BlogAPIListView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAutherOrReadOnly, ) # permissions.IsAuthenticated
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


