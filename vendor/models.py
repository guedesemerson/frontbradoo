from django.db import models
from localflavor.br.models import BRCNPJField

class Vendor(models.Model):
    name = models.CharField(max_length=150)
    cnpj = BRCNPJField(blank=False, null=False,unique=True)
    city = models.CharField(max_length=100, null=True, blank= True)


    def __str__(self):
        return self.name
