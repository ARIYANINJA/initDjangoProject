from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length = 120)
    desctiption = models.TextField(blank = True, null = True)
    price = models.DecimalField(decimal_places = 2, max_digits = 100000)
    summary = models.TextField(default = 'wow it works')