from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('deliveries', views.DeliveryView)

urlpatterns = [
    path('', include(router.urls)),
]
