from rest_framework import serializers
from apps.user.models import AccountUser
from apps.message.models import Message


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
