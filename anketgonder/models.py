from django.db import models
from django.contrib.auth.models import User
from anket.models import *

class Anket(models.Model):
    id = models.AutoField(primary_key=True)
    anket_adi = models.CharField(max_length=100)
    anket_soru_id = models.ManyToManyField(Sorular)
    anket_isci_id = models.ManyToManyField(Isciler)
    islem_tarihi = models.DateTimeField()
    kullanici_adi = models.CharField(max_length=50,default=User)

    def __str__(self):
        return self.anket_adi