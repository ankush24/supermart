from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=1, unique=True)
    price = models.IntegerField()
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name} - Rs {self.price}"

class Discount(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    min_discount_quantity = models.PositiveIntegerField()
    discount_price = models.IntegerField()

    def __str__(self):
        return f"{self.product.name} - Buy {self.min_discount_quantity} for Rs {self.discount_price}"

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity}x {self.product.name}" 
