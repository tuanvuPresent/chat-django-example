from rest_framework import serializers

from api.user.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('name',)
