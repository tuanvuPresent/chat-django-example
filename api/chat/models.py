from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Message(models.Model):
    author = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE, null=True)
    context = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
