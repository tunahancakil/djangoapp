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
    
    
    def  get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                'email_success/<int:element_id>',
                self.process_mail,
                name='mail',
            ),
            path(
                'sms_success/<int:element_id>',
                self.process_sms,
                name='sms',
            ),
        ]
        return custom_urls + urls


    def buttons(self,obj):
      
        return format_html(
            '<a id="{}" class="button" name="emailbutton" href="{}">Mail Gönder</a>&nbsp;'
            '<a id="{}" class="button" name="smsbutton" href="{}">Sms Gönder</a>',
            obj.id,
            reverse('admin:mail',args=[obj.id]),
            obj.id,
            reverse('admin:sms',args=[obj.id])
        ) 

    def process_mail(self, request, element_id):
        a = Anket.objects.get(id=element_id)
        for e in a.anket_isci_id.all():
            print(e.email)
            message= MIMEMultipart()
            message["From"] = "info@ttyazilim.net"  #Mail'i gönderen kişi
            message["To"] = "{}".format(e.email)  #Mail'i alan kişi
            message["Subject"] = "Python Smtp ile Mail Gönderme" #Mail'in konusu
            body= "{}Python üzerinde smtp modülü kullanarak mail gönderiyorum.".format(a.mail_mesaj)
            #Mail içerisinde yazacak içerik
            body_text = MIMEText(body,"plain") #
            message.attach(body_text)
            server = smtplib.SMTP()  
            server.connect("smtp.ttyazilim.net",587)
            server.login("info@ttyazilim.net","Tolgahan123+")
            try:
                server.sendmail(message["From"],message["To"],message.as_string())
            finally:
                print('quit')
                server.quit()
            
        return HttpResponse('Email gönderimi başarılı!{}'.format(id))

    def process_sms(self, request, element_id):
        a = Anket.objects.get(id=element_id)
        for e in a.anket_isci_id.all():
            print(e.iletisim_no)
            url = 'http://sms.corvass.net/json'
            myobj = {"Authentication": {           
                "apikey": "4775500361",           
                "apisecret": "0n6hu04dyiz23xyh9m6m"       },
                "message": "Deneme SMS",
                "msisdnArray": [e.iletisim_no],
                "originator": "TUNAHNCAKIL",
                "senddate": "",       
                "tags": ["Benipuanla.net"],
                "description": ""}
            x = requests.post(url, data = json.dumps(myobj))
        return HttpResponse('Sms gönderimi başarılı!')