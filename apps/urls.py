from django.conf.urls import url
from django.urls import include


urlpatterns = [
    url('', include('apps.chat.urls')),
    url('', include('apps.message.urls')),
    url('', include('apps.rooms.urls')),
    url('', include('apps.authentication.urls')),
]
