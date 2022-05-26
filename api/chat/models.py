from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Message(models.Model):
    channel = models.CharField(max_length=511, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
