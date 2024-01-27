from django.shortcuts import render
from rest_framework import viewsets
from .models import Delivery
from .serializers import DeliverySerializer


class DeliveryView(viewsets.ModelViewSet):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
