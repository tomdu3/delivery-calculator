from rest_framework import serializers
from .models import Delivery


class DeliveryFeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = (
            'cart_value',
            'delivery_distance',
            'number_of_items',
            'time'
        )

    def validate_cart_value(self, value):
        if value < 1:
            raise serializers.ValidationError("Cart value must be at least 1")
        return value

    def validate_delivery_distance(self, value):
        if value < 1:
            raise serializers.ValidationError("Delivery distance must be at least 1")
        return value

    def validate_number_of_items(self, value):
        if value < 1:
            raise serializers.ValidationError("Number of items must be at least 1")
        return value
