from rest_framework import routers

from apps.message import views

router = routers.SimpleRouter()
router.register('v1/messages', views.MessageModelViewSet, basename='messages')
urlpatterns = router.urls
