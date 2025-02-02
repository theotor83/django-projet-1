from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class TodoEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    dateCreated = models.DateTimeField(default=timezone.localtime(timezone.now()))
    completed = models.BooleanField(default=False)
