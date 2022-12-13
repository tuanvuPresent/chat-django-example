from rest_framework import serializers

from api.user.models import AccountUser


class AccountUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountUser
        fields = ('id', 'username')
