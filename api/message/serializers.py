from rest_framework import serializers

from api.message.models import Message
from api.user.serializers import AccountUserSerializer


class MessageSerializer(serializers.ModelSerializer):
    user = AccountUserSerializer()

    class Meta:
        model = Message
        fields = ('id', 'room', 'user', 'message', 'created_at')


class MessageCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ('id', 'room', 'user', 'message')
