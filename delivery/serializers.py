from rest_framework import serializers
from .models import Delivery


class DeliverySerializer(serializers.ModelSerializer):

    class Meta:
        model = Delivery
        fields = (
            'id',
            'cart_value',
            'delivery_distance',
            'number_of_items',
            'time',
            'delivery_fee'
        )


class DeliveryFeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = (
            'cart_value',
            'delivery_distance',
            'number_of_items',
            'time'
        )
