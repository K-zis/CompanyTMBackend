from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import TodoSerializer
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from .models import Todo


class TodoListCreate(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['title', 'content', 'completed']
    search_fields = ['title', 'content']
    ordering_fields = ['id', 'title']

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(author=user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)


class TodoUpdate(generics.UpdateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(author=user)


class TodoDelete(generics.DestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(author=user)
