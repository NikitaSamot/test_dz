from django.db import models


# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.CharField(max_length=50)


# Выборка только части колонок
products = Product.objects.values('name', 'price')
# Исключение определенных значений
excluded_products = Product.objects.exclude(category='Electronics')
