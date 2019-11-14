from django.contrib import admin
from .models import *


@admin.register(Kurumlar)
class KurumlarAdmin(admin.ModelAdmin):
    list_display  = ['unvan', 'email','islem_tarihi']
    list_filter = ['islem_tarihi']
    list_display_links = ('unvan', 'email')
    search_fields = ['unvan']
    list_per_page = (10)

@admin.register(Sorular)
class Sorular(admin.ModelAdmin):
    list_display = ['id','soru_baslik','soru_icerik','islem_tarihi']

@admin.register(Yoneticiler)
class Yoneticiler(admin.ModelAdmin):
    list_display = ['soyad','kurum',]

@admin.register(Isciler)
class Isciler(admin.ModelAdmin):
    list_display  = ['soyad','email','iletisim_no']
