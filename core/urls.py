from django.urls import path

from .views import BooksListView

app_name = 'core'

urlpatterns = [
    path('', BooksListView.as_view(), name='books'),
]