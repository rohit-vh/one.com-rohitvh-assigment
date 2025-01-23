from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField("Item name", max_length=40)
    description = models.CharField("Item description", max_length=100, blank=True, default='')
    rate = models.DecimalField("Price per unit", max_digits=6, decimal_places=2)
    veg = models.BooleanField("Is vegetarian dish?")

class CartItem(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField("Item quantity")

class Order(models.Model):
    created_at = models.DateTimeField("Order date and time", auto_now_add=True)
    customer_name = models.CharField("Customer name", max_length=40)
    cart = models.ManyToManyField(Product, through=CartItem)