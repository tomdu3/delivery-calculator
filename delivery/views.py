from django.views import View
from django.shortcuts import render
from rest_framework import viewsets, generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Delivery
from .serializers import DeliveryFeeSerializer
from .auxiliary import calculator


class CalculateDeliveryFeeView(APIView):
    serializer_class = DeliveryFeeSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            cart_value = serializer.validated_data['cart_value']
            delivery_distance = serializer.validated_data['delivery_distance']
            number_of_items = serializer.validated_data['number_of_items']
            time = serializer.validated_data['time']

            try:
                delivery_fee = calculator.calculate_delivery(
                    cart_value,
                    delivery_distance,
                    number_of_items,
                    time,
                )
                return Response(delivery_fee, status=status.HTTP_200_OK)
            except Exception as e:
                # Handle exceptions from the calculate function
                return Response(
                    {'error': str(e)},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            # Return serializer errors if the data is invalid
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
