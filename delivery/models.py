from django.db import models

# Create your models here.


class Delivery(models.Model):

    cart_value = models.IntegerField()
    delivery_distance = models.IntegerField()
    number_of_items = models.IntegerField()
    time = models.TimeField()
    delivery_fee = models.IntegerField()

    def __str__(self):
        return f'Delivery - {self.time} - {(self.delivery_fee/100):.2f}€'

    class Meta:
        db_table = 'delivery_delivery'
        verbose_name_plural = 'deliveries'
