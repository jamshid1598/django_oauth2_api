from rest_framework import serializers

from core.models import Library
from todo.models import ToDo
from blogapi.models import Blog

class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = '__all__' # ('name', 'description', 'price', 'image', 'imageURL', ) # this means,all fields of model Library is defined like ('name', 'description', 'price', 'image',) 

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'