from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    desctiption = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=100000)
    summary = models.TextField(default="wow it works")


class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.TextField()
    author = models.TextField()


class GeeksModel(models.Model):
    # fields of the model
    title = models.CharField(max_length=200)
    description = models.TextField()

    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.title
