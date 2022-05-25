from rest_framework import routers

from api.user import views

router = routers.DefaultRouter()
router.register('book', views.BookApiView, basename='book')
router.register('book2', views.Book2ApiView, basename='book2')
urlpatterns = router.urls
