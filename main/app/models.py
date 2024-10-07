from django.db import models


class Product(models.Model):
    GROUP_CHOICES = [
        ('Electronics', 'Electronics'),
        ('Clothing', 'Clothing'),
        ('Food', 'Food'),
    ]
    code = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    group = models.CharField(max_length=255, choices=GROUP_CHOICES)

    def __str__(self):
        return self.name


class Warehouse(models.Model):
    name = models.CharField(max_length=255)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.name
