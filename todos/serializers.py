from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["id", "title", "content", "completed", "created_at", "author"]
        extra_kwargs = {"author": {"read_only": True}}
