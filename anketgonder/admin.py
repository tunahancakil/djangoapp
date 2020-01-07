from django.contrib import admin
from django.template import loader
from django.utils.html import format_html
from django.core.mail import send_mail
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
import jwt
from  bitly_api import bitly_api

@admin.register(Anket)
class AnketGonderAdmin(admin.ModelAdmin):
    class Meta:
        model = Anket

    change_form_template = "button.html"    

    list_display = ['id','anket_adi','islem_tarihi','kullanici_adi','buttons']
    list_filter = ['islem_tarihi']
    
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
        key = 'secret'
        for e in a.anket_isci_id.all():
            print(e.email)
            encoded = jwt.encode({'isci_id': e.id,'anket_id':element_id}, key, algorithm='HS256')
            message= MIMEMultipart()
            message["From"] = "info@ttyazilim.net"  #Mail'i gönderen kişi
            message["To"] = "{}".format(e.email)  #Mail'i alan kişi
            message["Subject"] = "Benipuanla.net - Anket" #Mail'in konusu
            print(str(encoded)[2:-1])
            body = loader.render_to_string('email.html',{'link': 'http://www.benipuanla.net/tema/anket/' + str(encoded)[2:-1]})
            try:
                send_mail(message['Subject'],"",message["From"],[message["To"]],html_message=body)
            finally:
                print('quit')
        return HttpResponse('Email gönderimi başarılı!{}'.format(id))

    def process_sms(self, request, element_id):
        a = Anket.objects.get(id=element_id)
        key = 'secret'
        for e in a.anket_isci_id.all():
            encoded = jwt.encode({'isci_id': e.id,'anket_id':element_id}, key, algorithm='HS256')
            b = bitly_api.Connection(access_token="655c090ad60a21d1db57b9b66873783b7345e38a")
            response_ = b.shorten('http://www.benipuanla.net/tema/anket/' + str(encoded)[2:-1])
            print(response_.get('url'))
            response_url = str(response_.get('url'))
            url = 'http://sms.corvass.net/json'
            myobj = {"Authentication": {           
                "apikey": "4775500361",           
                "apisecret": "0n6hu04dyiz23xyh9m6m"       },
                "message": "Anketinize ulaşmak için aşağıdaki linke tıklayınız. {}".format(response_url),
                "msisdnArray": [e.iletisim_no],
                "originator": "TUNAHNCAKIL",
                "senddate": "",       
                "tags": ["Benipuanla.net"],
                "description": ""}
            x = requests.post(url, data = json.dumps(myobj))
        return HttpResponse('Sms gönderimi başarılı!')


