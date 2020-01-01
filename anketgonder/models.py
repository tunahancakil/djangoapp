from django.db import models
from django.contrib.auth.models import User
from anket.models import *
from django.contrib import admin


class Anket(models.Model):
    id = models.AutoField(primary_key=True)
    anket_adi = models.CharField(max_length=100)
    anket_soru_id = models.ManyToManyField(Sorular)
    anket_isci_id = models.ManyToManyField(Isciler)
    mail_mesaj = models.TextField(max_length=500,null=True)
    subject = models.CharField(max_length=100,null=True)
    islem_tarihi = models.DateTimeField(auto_now_add=True)
    kullanici_adi = models.CharField(max_length=50,default=User)

    def __int__(self):
        return "%s %s %s" % (self.id, self.anket_soru_id, self.anket_isci_id)

class Cevaplar(models.Model):
    id = models.AutoField(primary_key=True)
    deger = forms.ChoiceField(widget=forms.RadioSelect)
    anket_soru_id = models.ForeignKey(Sorular, on_delete=models.CASCADE)
    anket_isci_id = models.ForeignKey(Isciler, on_delete=models.CASCADE)
    islem_tarihi = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "%s %s %s %s"  % (self.id,self.deger,self.anket_soru_id, self.anket_isci_id)