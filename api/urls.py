from django.urls import path

from .views import LibraryAPIView

app_name = 'api'

urlpatterns = [
    path('', LibraryAPIView.as_view(), name='book_api'),
]