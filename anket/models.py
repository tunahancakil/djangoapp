from django.db import models
from django.utils import timezone

class Kurumlar(models.Model):
    id = models.AutoField(primary_key=True)
    unvan = models.CharField(max_length=250,verbose_name="İş Yeri Ünvanı")
    iletisim_no = models.CharField(max_length=10,verbose_name="İletişim No")
    email = models.EmailField(max_length=50)    
    puan = models.IntegerField(default=0)
    islem_tarihi = models.DateTimeField()
    kullanici_adi = models.CharField(max_length=50)

    def __str__(self):
        return self.unvan
        
class Yoneticiler(models.Model):
    id = models.AutoField(primary_key=True)
    ad = models.CharField(max_length=50,verbose_name="Yönetici Ad")
    soyad = models.CharField(max_length=50,verbose_name="Yönetici Soyad")
    email = models.EmailField(max_length=50)
    iletisim_no = models.CharField(max_length=10,verbose_name="İletişim No")
    kurum = models.ForeignKey(Kurumlar, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s %s" % (self.ad, self.soyad, self.kurum.unvan)

class Isciler(models.Model):
    id = models.AutoField(primary_key=True)
    ad = models.CharField(max_length=50,verbose_name="Ad")
    soyad = models.CharField(max_length=50,verbose_name="Soyad")
    email = models.EmailField(max_length=50)
    iletisim_no = models.CharField(max_length=10,verbose_name="İletişim No")
    yonetici = models.ManyToManyField(Yoneticiler)
    kurum = models.ForeignKey(Kurumlar, on_delete=models.CASCADE)
    islem_tarihi = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return "%s %s %s %s" % (self.id,self.ad,self.soyad,self.email)


class Sorular(models.Model):
    id = models.AutoField(primary_key=True)
    soru_baslik = models.CharField(max_length=250,verbose_name="Soru Grubu")
    soru_icerik = models.TextField(verbose_name="Soru İçerik")
    cevap = models.IntegerField(editable=True)
    islem_tarihi = models.DateTimeField(auto_now_add=True)
    kullanici_adi = models.CharField("auth.user",max_length=50)

    def __str__(self):
        return "%s %s" % (self.id,self.soru_icerik)