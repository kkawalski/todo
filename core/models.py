from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    def __str__(self):
        return self.email


class Todo(models.Model):
    user = models.ForeignKey('core.User', on_delete=models.CASCADE, related_name='todos')

    title = models.CharField(max_length=50)
    text = models.CharField(max_length=255)

    is_active = models.BooleanField(default=True)
    is_done = models.BooleanField(default=False)

    created_date = models.DateTimeField(auto_now_add=True)
    done_date = models.DateTimeField()

    def __str__(self):
        return f'{self.user.email}, {self.title}'
