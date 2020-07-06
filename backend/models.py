from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Group

# Create your models here.

class Log(models.Model):
    created_by = models.ForeignKey(User, default=None, on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.created