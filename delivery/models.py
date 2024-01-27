from django.db import models

# Create your models here.


class Delivery(models.Model):

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
