from rest_framework import routers

from api.message import views

router = routers.SimpleRouter()
router.register('v1/message', views.MessageModelViewSet, basename='message')
urlpatterns = router.urls
