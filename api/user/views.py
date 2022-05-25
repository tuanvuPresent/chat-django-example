# Create your views here.
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from api.user.models import Book
from api.user.repository import BookRepository
from api.user.serializers import BookSerializer
from api.user.signal import get_book


class BookApiView(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    post_repository = BookRepository()

    @action(methods=['GET'], detail=False, url_path='example')
    def example(self, request):
        posts = self.post_repository.get_all()
        serializer = BookSerializer(posts, many=True)

        get_book.send(sender=self.__class__, a=1, b=2)

        return Response(serializer.data)


class Book2ApiView(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
