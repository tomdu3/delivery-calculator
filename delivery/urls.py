from django.urls import path
from . import views

# open the API POST request page on the root path
urlpatterns = [
    path('', views.CalculateDeliveryFeeView.as_view(), name='calculate_delivery_fee'),
]
