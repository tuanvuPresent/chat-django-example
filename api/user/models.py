from api.core.uuid_model import UuidModel
from django.contrib.auth.models import AbstractUser
from django.db import models


class AccountUser(UuidModel, AbstractUser):
    username = models.CharField(max_length=64, unique=True)

    class Meta:
        db_table = 'chat_user'