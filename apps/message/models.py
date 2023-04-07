from django.db import models
from apps.core.uuid_model import UuidModel
from apps.rooms.models import Room
from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.message.utils import send_message_websocket
from django.conf import settings


class Message(UuidModel):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'chat_message'


@receiver(post_save, sender=Message)
def message_post_save(sender, instance, **kwargs):
    send_message_websocket(message=instance.message, channel=instance.room_id)
