from django.db import models
from django.utils import timezone


# Create your models here.

class Board(models.Model):
    name = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    board = models.ForeignKey('Board', related_name='tasks', on_delete=models.CASCADE)
