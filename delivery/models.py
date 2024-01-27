from django.db import models


class Delivery(models.Model):
    """
    Model for Delivery. Can be used to save the records and for the JSON
    serializers for the API requests/responses.
    """
    cart_value = models.IntegerField(null=False)
    delivery_distance = models.IntegerField(null=False)
    number_of_items = models.IntegerField(null=False)
    time = models.CharField(max_length=50)
    delivery_fee = models.IntegerField(null=True, default=0)

    def __str__(self):
        return f'Delivery - {self.time} - {(self.delivery_fee/100):.2f}€'

    class Meta:
        db_table = 'delivery_delivery'
        verbose_name_plural = 'deliveries'
