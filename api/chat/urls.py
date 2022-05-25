from django.urls import path

from . import views
from .comsumers import ChatConsumer

urlpatterns = [
    path('chat', views.index, name='index'),
    path('chat/<room_name>/', views.room, name='room'),
]
websocket_urlpatterns = [
    path('ws/chat/<room_name>/', ChatConsumer.as_asgi()),
]
