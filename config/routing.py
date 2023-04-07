from apps.chat.middleware import TokenAuthMiddleWare
from channels.routing import ProtocolTypeRouter, URLRouter

from apps.chat.urls import websocket_urlpatterns

application = ProtocolTypeRouter({
    'websocket': TokenAuthMiddleWare(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})
