from django.db import models
from api.core.uuid_model import UuidModel
from api.user.models import AccountUser
from api.room.models import Room
from django.db.models.signals import post_save
from django.dispatch import receiver
from api.message.utils import send_message_websocket


class Message(UuidModel):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(AccountUser, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'chat_message'


@receiver(post_save, sender=Message)
def message_post_save(sender, instance, **kwargs):
    send_message_websocket(message=instance.message, channel=instance.room_id)