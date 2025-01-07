from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    name = models.CharField(max_length=200)
    addressline1 = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    postcode = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    active = models.BooleanField()
    creditlimit = models.IntegerField()
    notes = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="customer")
