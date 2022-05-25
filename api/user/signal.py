import django.dispatch
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

get_book = django.dispatch.Signal(providing_args=["kwargs"])


@receiver(post_save, sender=User)
def get_book_all_receiver(sender, **kwargs):
    print(sender, kwargs)
