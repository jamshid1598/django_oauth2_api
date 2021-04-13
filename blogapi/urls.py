from django.urls import path

from .views import (
    BlogAPIListView,
    BlogAPIDetailView,
)

app_name = 'blog'

urlpatterns = [
    path('', BlogAPIListView.as_view(), name='blog-list'),
    path('<int:pk>/', BlogAPIDetailView.as_view(), name='blog-detail'),
]