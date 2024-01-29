from django.test import TestCase
from delivery.serializers import DeliveryFeeSerializer


class DeliveryFeeSerializerTestCase(TestCase):
    """
    Test cases for the DeliveryFeeSerializer class
    """
    valid_data = {
            "cart_value": 790,
            "delivery_distance": 2235,
            "number_of_items": 4,
            "time": "2024-01-15T13:00:00Z"
            }  # data sample

    def test_valid_data(self):
        # Test the serializer with valid data
        valid_data = self.valid_data.copy()  # copy the valid data sample
        serializer = DeliveryFeeSerializer(data=valid_data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_cart_value(self):
        # Test the serializer with invalid data
        invalid_data = self.valid_data.copy()  # copy the valid data sample
        invalid_data['cart_value'] = 0  # invalid cart value
        serializer = DeliveryFeeSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('cart_value', serializer.errors)

    def test_invalid_delivery_distance_value(self):
        # Test the serializer with invalid data
        invalid_data = self.valid_data.copy()  # copy the valid data sample
        invalid_data['delivery_distance'] = 0  # invalid distance value
        serializer = DeliveryFeeSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('delivery_distance', serializer.errors)

    def test_invalid_number_of_items(self):
        # Test the serializer with invalid data
        invalid_data = self.valid_data.copy()  # copy the valid data sample
        invalid_data['number_of_items'] = 0  # invalid number of items
        serializer = DeliveryFeeSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('number_of_items', serializer.errors)

    def test_invalid_time_string_format(self):
        # Test the serializer with invalid data
        invalid_data = self.valid_data.copy()  # copy the valid data sample
        invalid_data['time'] = 'something'  # invalid time stamp
        serializer = DeliveryFeeSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('time', serializer.errors)
