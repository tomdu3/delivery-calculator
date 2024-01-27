from django.urls import path, include
from . import views
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register('deliveries', views.DeliveryView)
# router.register('calculate_delivery_fee', views.CalculateDeliveryFeeView)

urlpatterns = [
    # path('', include(router.urls)),
    path('calculate_delivery_fee', views.CalculateDeliveryFeeView.as_view(), name='calculate_delivery_fee'),
]
