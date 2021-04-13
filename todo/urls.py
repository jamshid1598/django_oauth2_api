from django.urls import path

from .views import (
    ToDoAPIListView,
    ToDoAPIDetailView,
)

app_name='todo'

urlpatterns = [
    path('', ToDoAPIListView.as_view(), name='todo-list'),
    path('detail/<int:pk>/', ToDoAPIDetailView.as_view(), name='todo-detail'),
]