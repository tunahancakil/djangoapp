from django.contrib import admin
from django.utils.html import format_html
from .models import *
from django.urls import reverse,path
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys


@admin.register(Anket)
class AnketGonderAdmin(admin.ModelAdmin):

    list_display = ['anket_adi','islem_tarihi','kullanici_adi','smsbutton']
    list_filter = ['islem_tarihi']

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                'email_success/',
                self.process_sms,
                name='mail',
            ),
            path(
                '/sms_success',
                self.process_sms,
                name='sms',
            ),
        ]
        return custom_urls + urls


    def smsbutton(self,event=None):
        return format_html(
            '<a class="button" href="{}">Mail Gönder</a>&nbsp;'
            '<a class="button" href="{}">Sms Gönder</a>',
            reverse('admin:mail'),
            reverse('admin:sms'),
        ) 
   
    

    def process_sms(self, request, **kwargs):
        message= MIMEMultipart()   
        message["From"] = "info@ttyazilim.net"  #Mail'i gönderen kişi
        message["To"] = "tunahancakil@gmail.com"    #Mail'i alan kişi
        message["Subject"] = "Python Smtp ile Mail Gönderme" #Mail'in konusu
        body= """
        Python üzerinde smtp modülü
        kullanarak mail gönderiyorum.
        """   #Mail içerisinde yazacak içerik
        body_text = MIMEText(body,"plain") #
        message.attach(body_text)
        #Gmail serverlerine bağlanma işlemi.
        print('here1')
        server = smtplib.SMTP("smtp.ttyazilim.net",587)  
        server.connect()
        print('here2')
        server.login("info@ttyazilim.net","Tolgahan123+")
        server.set_debuglevel(false)
        try:
            server.sendmail(message["From"],message["To"],message.as_string())
        finally:
            print('quit')
            server.quit()
