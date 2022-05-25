from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class TimeStampManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(deleted_at=None)

    def get_test(self):
        pass


class TimeStampModels(models.Model):
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    objects = TimeStampManager()

    class Meta:
        abstract = True


class Book(TimeStampModels):
    name = models.CharField(max_length=128)

    class Meta:
        db_table = 'books'
