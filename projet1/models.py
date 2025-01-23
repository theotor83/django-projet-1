from django.db import models
from django.utils import timezone


# Create your models here.

class TodoEntry(models.Model):
    name = models.CharField(max_length=100)
    dateCreated = models.DateTimeField(default=timezone.now)
    completed = models.BooleanField(default=False)
