from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import transaction
from django.db.models import Max
import secrets

# Create your models here.

class TodoEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    entryid = models.PositiveIntegerField(null=True)
    name = models.CharField(max_length=255)
    dateCreated = models.DateTimeField(default=timezone.now)
    completed = models.BooleanField(default=False)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'entryid'],
                name='unique_user_entryid'
            )
        ]

    def save(self, *args, **kwargs):
        if self.pk is None:  # Only during creation
            with transaction.atomic():
                # Lock the user row to prevent concurrent entryid generation
                user = User.objects.select_for_update().get(pk=self.user_id)
                max_entryid = TodoEntry.objects.filter(
                    user=user
                ).aggregate(max_entryid=Max('entryid'))['max_entryid'] or 0
                self.entryid = max_entryid + 1
        super().save(*args, **kwargs)

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
