from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
) 


from .models import ToDo
from api.serializers import ToDoSerializer

# Create your views here.


class ToDoAPIListView(ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


class ToDoAPIDetailView(RetrieveAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer