from django.shortcuts import render
from django.views.generic import ListView

from .models import Library
# Create your views here.


class BooksListView(ListView):
    model = Library
    template_name = 'index.html'