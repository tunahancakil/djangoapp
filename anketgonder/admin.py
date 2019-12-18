from django.contrib import admin
from django.utils.html import format_html
from .models import *

@admin.register(Anket)
class AnketGonderAdmin(admin.ModelAdmin):
    def smsbutton(self,event=None):
        return format_html(
            '<div class="submit-rov"><form action="mail.py">'
            '<input type="submit" value="Submit">'
            '</form></div>'
        ) 
    def emailbutton(self,event=None):
        return format_html(
            '<div class="submit-rov"><form action="/action_page.php">'
            '<input type="submit" value="Submit">'
            '</form></div>'
        )
    list_display = ['anket_adi','islem_tarihi','kullanici_adi','smsbutton','emailbutton']
    list_filter = ['islem_tarihi']

    
