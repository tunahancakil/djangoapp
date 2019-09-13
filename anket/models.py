from django.db import models
from django.utils import timezone

class UyeKurumlar(models.Model):
    id = models.AutoField(primary_key=True)
    unvan = models.CharField(max_length=250,verbose_name="İş Yeri Ünvanı")
    iletisim_no = models.CharField(max_length=250)
    email = models.EmailField(max_length=50)    
    puan = models.IntegerField(editable=True)
    islem_tarihi = models.DateTimeField()
    kullanici_adi = models.CharField(max_length=50)

    def __str__(self):
        return self.unvan

class Sorular(models.Model):
    id = models.AutoField(primary_key=True)
    soru_baslik = models.CharField(max_length=250,verbose_name="Soru Grubu")
    soru_icerik = models.TextField(verbose_name="Soru İçerik")
    cevap = models.IntegerField(editable=True)
    islem_tarihi = models.DateTimeField()
    kullanici_adi = models.CharField(max_length=50)