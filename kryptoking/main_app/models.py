from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Krypto(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    information = models.CharField(max_length=250)
    symbol = models.CharField(max_length=50)

    def __str__(self):
        return self.name