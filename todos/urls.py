from django.urls import path
from . import api

urlpatterns = [
    path("", api.TodoListCreate.as_view(), name="Todo-list"),
    path("update/<int:pk>/", api.TodoUpdate.as_view(), name="update-todo"),
    path("delete/<int:pk>/", api.TodoDelete.as_view(), name="delete-todo")
]
