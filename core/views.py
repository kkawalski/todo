from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import UserSerializer, TodoBaseSerializer, TodoSerializer
from .models import User, Todo


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self):
        queryset = self.queryset.filter(id=self.request.user.id)
        return queryset

    @action(detail=False)
    def me(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class TodoView(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def get_serializer_class(self):
        if self.action == 'list':
            return TodoBaseSerializer
        return self.serializer_class

    def get_queryset(self):
        queryset = self.queryset.filter(is_active=True)
        user = self.request.user
        return queryset.filter(user=user)

    @action(methods=['patch'], detail=True)
    def done(self, request, *args, **kwargs):
        todo = self.get_object()
        todo.is_done = True
        todo.save()
        return Response(status=status.HTTP_200_OK)
