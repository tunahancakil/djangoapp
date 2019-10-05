from django.contrib import admin
from .models import *


@admin.register(UyeKurumlar)
class UyeKurumlarAdmin(admin.ModelAdmin):
    list_display  = ['unvan', 'email','islem_tarihi']
    list_filter = ['islem_tarihi']
    list_display_links = ('unvan', 'email')
    search_fields = ['unvan']
    list_per_page = (10)


@admin.register(Sorular)
class Sorular(admin.ModelAdmin):
    list_display = ['soru_baslik','soru_icerik','islem_tarihi']

@admin.register(Yoneticiler)
class Yoneticiler(admin.ModelAdmin):
    list_display = ['id','yonetici_ad','yonetici_soyad']
