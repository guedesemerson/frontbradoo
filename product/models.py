from django.db import models
from vendor.models import Vendor


class Product(models.Model):
    name = models.CharField(max_length=150)
    code = models.IntegerField()
    price = models.DecimalField(max_digits=9,decimal_places=2, null=True, blank= True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
