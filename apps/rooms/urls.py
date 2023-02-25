from rest_framework import routers

from apps.rooms import views

router = routers.SimpleRouter()
router.register('v1/rooms', views.RoomModelViewSet, basename='rooms')
urlpatterns = router.urls
