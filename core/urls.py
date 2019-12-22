from rest_framework.routers import DefaultRouter

from django.urls import path, include

from .views import UserView, TodoView

router = DefaultRouter()
router.register('todos', TodoView, basename='todos')
router.register('users', UserView, basename='users')

urlpatterns = [
    path('', include(router.urls)),
]
