from django.test import SimpleTestCase
from django.urls import reverse, resolve
from delivery.views import CalculateDeliveryFeeView


class URLTestCase(SimpleTestCase):
    def test_calculate_delivery_fee_url(self):
        """
        Test whether the root URL ('/') is correctly resolved to 
        CalculateDeliveryFeeView.
        """
        url = reverse('calculate_delivery_fee')
        self.assertEqual(resolve(url).func.view_class, CalculateDeliveryFeeView)
