from django.conf.urls import url
from django.urls import include


urlpatterns = [
    url('', include('api.chat.urls')),
    url('', include('api.message.urls')),
    url('', include('api.room.urls')),
]
