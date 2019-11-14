from django.db import models
from django.contrib.auth.models import User
from ../anket/models import Sorular

class Anket(models.Model):
    id = models.AutoField(primary_key=True)
    anket_adi = model.CharField(max_length=100)
    anket_soru_id = models.ManyToManyField(Sorular)
    islem_tarihi = models.DateTimeField()
    kullanici_adi = models.CharField(max_length=50,default=request.user)

    def __str__(self):
        return self.anket_adi