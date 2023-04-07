# Create your views here.
from datetime import datetime

from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from .cache import UserActivityStore
from .serializer import JWTLoginSerializer, UserAccountSerializer
from rest_framework.viewsets import GenericViewSet


class JWTAuthAPIView(GenericViewSet):
    serializer_class = JWTLoginSerializer

    @action(methods=['post'], detail=False)
    def logout(self, request):
        response = Response(data=None)
        if request.user.is_authenticated:
            UserActivityStore(request.user).logged_out()
            
        if api_settings.JWT_AUTH_COOKIE:
            response.delete_cookie(api_settings.JWT_AUTH_COOKIE)
        return response

    @swagger_auto_schema(request_body=JWTLoginSerializer)
    @action(methods=['post'], detail=False, authentication_classes=[], permission_classes=[])
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data.get('user')
        token = serializer.validated_data.get('token')

        data = {
            'token': token,
            'user': UserAccountSerializer(user).data
        }
        response = Response(data=data)
        if api_settings.JWT_AUTH_COOKIE:
            expiration = (datetime.utcnow() +
                          api_settings.JWT_EXPIRATION_DELTA)
            response.set_cookie(api_settings.JWT_AUTH_COOKIE,
                                token,
                                expires=expiration,
                                httponly=True)

        return response