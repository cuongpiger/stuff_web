from django.db import models
from cart.models import Cart

from user.models import CustomerUser

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    shipping_address = models.CharField(max_length=255, default='')
    order_description = models.TextField(default='')
    is_completed = models.BooleanField(default=False)
    