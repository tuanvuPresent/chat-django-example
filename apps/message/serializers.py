from rest_framework import serializers
from apps.message.models import Message
from django.contrib.auth import get_user_model

AccountUser = get_user_model()

class AccountUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountUser
        fields = ('id', 'username')


class MessageSerializer(serializers.ModelSerializer):
    user = AccountUserSerializer()

    class Meta:
        model = Message
        fields = ('id', 'room', 'user', 'message', 'created_at')


class MessageCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ('id', 'room', 'user', 'message')
