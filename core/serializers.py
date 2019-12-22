from rest_framework import serializers

from .models import Todo, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
        ]


class TodoBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = [
            'id',
            'title',
            'is_done',
        ]


class TodoSerializer(TodoBaseSerializer):
    user = UserSerializer()

    class Meta(TodoBaseSerializer.Meta):
        fields = TodoBaseSerializer.Meta.fields + [
            'text',
            'user',
        ]
