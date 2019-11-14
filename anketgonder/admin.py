from django.contrib import admin
from django.utils.html import format_html
from .models import *

@admin.register(Anket)
class AnketGonderAdmin(admin.ModelAdmin):
    def button(self,event=None):
        return format_html(
            '<div class="submit-rov"><a href="http://okandiyebiri.com"><input type="submit" value="Gönder" /></a></div>'
        ) 

    list_display = ['anket_adi','islem_tarihi','kullanici_adi','button']
    list_filter = ['islem_tarihi']

    
