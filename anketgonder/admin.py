from django.contrib import admin
from django.utils.html import format_html
from .models import *
from anket.models import *
from django.urls import reverse,path
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
from django.http import HttpResponse
from django import forms
import json
import requests
import urllib

@admin.register(Anket)
class AnketGonderAdmin(admin.ModelAdmin):
    class Meta:
        model = Anket

    change_form_template = "button.html"    

    list_display = ['id','anket_adi','islem_tarihi','kullanici_adi','buttons']
    list_filter = ['islem_tarihi']

    def response_change(self, request, obj):
        if "_make-unique" in request.POST:
            matching_names_except_this = self.get_queryset(request).filter(name=obj.name).exclude(pk=obj.id)
            print(obj.anket_isci_id)
            return HttpResponseRedirect(".")
        return super().response_change(request, obj)     
    
    
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                'email_success/',
                self.process_mail,
                name='mail',
            ),
            path(
                'sms_success/',
                self.process_sms,
                name='sms',
            ),
        ]
        return custom_urls + urls


    def buttons(self,obj):
        print(obj)
        return format_html(
            '<a id="{}" class="button" href="{}">Mail Gönder</a>&nbsp;'
            '<a id="{}" class="button" href="{}">Sms Gönder</a>',
            obj.id,
            reverse('admin:mail'),
            obj.id,
            reverse('admin:sms')
        ) 
   
    

    def process_mail(self, request,*args, **kwargs):
        message= MIMEMultipart()  
        message["From"] = "info@ttyazilim.net"  #Mail'i gönderen kişi
        message["To"] = "tunahancakil@gmail.com"    #Mail'i alan kişi
        message["Subject"] = "Python Smtp ile Mail Gönderme" #Mail'in konusu
        body= "{}Python üzerinde smtp modülü kullanarak mail gönderiyorum."
        #Mail içerisinde yazacak içerik
        print(body)
        body_text = MIMEText(body,"plain") #
        message.attach(body_text)
        #Gmail serverlerine bağlanma işlemi.
        print('here1')
        server = smtplib.SMTP()  
        server.connect("smtp.ttyazilim.net",587)
        print('here2')
        server.login("info@ttyazilim.net","Tolgahan123+")
        try:
            server.sendmail(message["From"],message["To"],message.as_string())
        finally:
            print('quit')
            server.quit()
        return HttpResponse('Email gönderimi başarılı!')



    def process_sms(self, request,*args, **kwargs):
    
        url = 'http://sms.corvass.net/json'
        myobj = {"Authentication": {           
             "apikey": "4775500361",           
             "apisecret": "0n6hu04dyiz23xyh9m6m"       },
             "message": "Benipuanla.net anket linkinize tıklayarak puanlamaya başlayabilirsiniz.",
             "msisdnArray": ["5318985507", "05393239896", "905455860993","05554861373"],
             "originator": "TUNAHNCAKIL",
             "senddate": "",       
             "tags": ["deneme", "tayfun", "tunahan", "MERT"],
             "description": ""}
        x = requests.post(url, data = json.dumps(myobj))
        return HttpResponse('Sms gönderimi başarılı!')