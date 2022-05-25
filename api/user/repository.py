from api.user.models import Book


class BookRepository:
    def get_all(self):
        return Book.objects.all()

    def find(self, id):
        return []

    def save(self, data):
        return []
