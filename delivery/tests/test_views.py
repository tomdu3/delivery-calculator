from rest_framework.test import APITestCase, APIClient
from rest_framework import status


class CalculateDeliveryFeeViewTestCase(APITestCase):
    """
    Test case for the CalculateDeliveryFeeView
    """

    def setUp(self):
        self.client = APIClient()

    def test_post_valid_data_sample1(self):
        # Test the view with valid data (sample 1)
        valid_data = {
            'cart_value': 790,
            'delivery_distance': 2235,
            'number_of_items': 4,
            'time': '2024-01-15T13:00:00Z'
        }
        expected_response = {
            'delivery_fee': 710,
        }
        response = self.client.post('/', valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), expected_response)

    def test_post_valid_data_sample2(self):
        # Test the view with valid data (sample 2)
        valid_data = {
            'cart_value': 2000,
            'delivery_distance': 900,
            'number_of_items': 1,
            'time': '2021-10-21T17:00:00Z'
        }
        expected_response = {
            'delivery_fee': 200,
        }
        response = self.client.post('/', valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), expected_response)

    def test_post_invalid_data(self):
        # Test the view with invalid data
        invalid_data = {
            'cart_value': 0,  # invalid cart value
            'delivery_distance': 10,
            'number_of_items': 1,
            'time': '2024-01-15T13:00:00Z'
        }
        response = self.client.post('/', invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # Check for cart_value in response errors
        self.assertIn('cart_value', response.json())
