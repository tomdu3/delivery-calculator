from rest_framework import serializers
from datetime import datetime
from .models import Delivery


class DeliveryFeeSerializer(serializers.ModelSerializer):
    """
    Defining the input fields for the JSON API request
    """
    class Meta:
        model = Delivery
        fields = (
            'cart_value',
            'delivery_distance',
            'number_of_items',
            'time'
        )

    def validate_cart_value(self, value):
        """
        Validation for the API request input: cart_value. The value cannot be
        less than 1.
        """
        if value < 1:
            raise serializers.ValidationError(
                'Cart value must be at least 1'
            )
        return value

    def validate_delivery_distance(self, value):
        """
        Validation for the API request input: delivery_distance. The value
        cannot be less than 1.
        """
        if value < 1:
            raise serializers.ValidationError(
                'Delivery distance must be at least 1'
            )
        return value

    def validate_number_of_items(self, value):
        """
        Validation for the API request input: number_of_items. The value
        cannot be less than 1.
        """
        if value < 1:
            raise serializers.ValidationError(
                'Number of items must be at least 1'
            )
        return value

    def validate_time(self, value):
        """
        Validation for the API request input: time. The value must be a proper
        ISO format string.
        """
        try:
            # Attempt to parse the time string to a datetime object
            datetime.fromisoformat(value)
        except ValueError:
            # If parsing fails, raise a validation error
            raise serializers.ValidationError(
                'Time must be a valid ISO format string'
            )
        return value
