from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import secrets

# Create your models here.

class TodoEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    dateCreated = models.DateTimeField(default=timezone.localtime(timezone.now()))
    completed = models.BooleanField(default=False)

class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    key = models.CharField(max_length=50, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super().save(*args, **kwargs)

    @staticmethod
    def generate_key():
        return secrets.token_urlsafe(30)
