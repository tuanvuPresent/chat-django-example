from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('auth', views.JWTAuthAPIView, basename='auth')
urlpatterns = router.urls
