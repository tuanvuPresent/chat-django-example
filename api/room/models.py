from api.core.uuid_model import UuidModel
from django.db import models


class Room(UuidModel):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'chat_room'
