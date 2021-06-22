from django.db import models
from django.utils import timezone

# Create your models here.
class Products(models.Model):
    productName = models.CharField(max_length=200)
    productImage = models.ImageField()

class Customer(models.Model):
    customerFirstName = models.CharField(max_length=200)
    customerLastName = models.CharField(max_length=200)
    purchasedProducts = models.ManyToManyField(Products)
    dateJoined = models.DateTimeField('Date User Joined')



