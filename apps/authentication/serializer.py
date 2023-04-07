from django.contrib.auth import authenticate
from rest_framework import serializers

from django.contrib.auth import get_user_model
from .utils import JwtTokenGenerator

User = get_user_model()


class JWTLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=64, required=True)
    password = serializers.CharField(max_length=64, required=True, help_text='Leave empty if no change needed',
                                     style={'input_type': 'password'})

    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)

        if not username or not password:
            raise serializers.ValidationError(
                'password and username field required')

        user = authenticate(username=username, password=password)
        if not user:
            raise serializers.ValidationError(
                'Tên đăng nhập hoặc mật khẩu không đúng')

        token_generator = JwtTokenGenerator()
        token = token_generator.get_token(user)
        user.sid = token_generator.jti
        return {
            'user': user,
            'token': token
        }


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']
