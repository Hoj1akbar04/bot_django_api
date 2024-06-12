from django.db import models


class Users(models.Model):
    full_name = models.CharField(max_length=50, null=True, blank=False)
    username = models.CharField(max_length=30, null=True, unique=True)
    telegram_id = models.PositiveBigIntegerField(unique=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class Product(models.Model):
    name = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(null=True)
    category_code = models.CharField(max_length=20)
    category_name = models.CharField(max_length=30)
    subcategory_code = models.CharField(max_length=20)
    subcategory_name = models.CharField(max_length=20)

    def __str__(self):
        return self.name