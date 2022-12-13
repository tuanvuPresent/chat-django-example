from rest_framework import routers

from api.room import views

router = routers.SimpleRouter()
router.register('v1/room', views.RoomModelViewSet, basename='room')
urlpatterns = router.urls
