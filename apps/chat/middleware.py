from channels.db import database_sync_to_async
from channels.routing import ProtocolTypeRouter, URLRouter
from django.contrib.auth.models import AnonymousUser
from django.urls import path
from apps.authentication.utils import JwtTokenGenerator
from django.contrib.auth import get_user_model

User = get_user_model()

@database_sync_to_async
def get_user(user_id):
    try:
        user = User.objects.get(id=user_id)
    except Exception:
        user = AnonymousUser()
    return user


class TokenAuthMiddleWare:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        try:
            query_params = dict((x.split('=')
                                for x in scope['query_string'].decode().split("&")))
            token = query_params.get('token')
        except ValueError:
            token = None

        try:
            token_generator = JwtTokenGenerator()
            token_generator.verify_token(token)
            scope["user"] = await get_user(token_generator.user_id)
        except Exception:
            scope["user"] = None
        return await self.app(scope, receive, send)
