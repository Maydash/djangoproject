from django.db import models
# from products.models import Product


class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    description = models.TextField(null=True, blank=False)
    quantity = models.PositiveIntegerField(default=0, blank=True)
    group = models.ForeignKey('products.Group', on_delete=models.PROTECT, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} : {self.price} : {self.description}'


class Group(models.Model):
    title = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return f'{self.title} : {self.code}'


