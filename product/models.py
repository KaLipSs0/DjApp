from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=256)
    price = models.FloatField()
    brand = models.ForeignKey('Brand', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name
