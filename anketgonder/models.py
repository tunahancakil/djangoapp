from django.db import models
from django.contrib.auth.models import User
from anket.models import *
from django.contrib import admin
from django.utils.html import format_html
from .models import *
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


def buttons(self,event=None):
    anket_id = Anket.objects.get(id=1)
    return format_html(
        '<a class="button" href="{}">Mail Gönder</a>&nbsp;'
        '<a id="{}" class="button" href="{}">Sms Gönder</a>',
            
        reverse('admin:mail'),
        format(anket_id),
        reverse('admin:sms'),
    ) 

def process_mail(self, request,*args, **kwargs):
    anket_id = Anket.objects.get(id=1)
    message= MIMEMultipart()   
    message["From"] = "info@ttyazilim.net"  #Mail'i gönderen kişi
    message["To"] = "tunahancakil@gmail.com"    #Mail'i alan kişi
    message["Subject"] = "Python Smtp ile Mail Gönderme" #Mail'in konusu
    body= "{}Python üzerinde smtp modülü kullanarak mail gönderiyorum.".format(anket_id)
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
    
    url = 'http://sms.corvass.net/jsona'
    myobj = {"Authentication": {           
        "apikey": "4775500361",           
        "apisecret": "0n6hu04dyiz23xyh9m6m"       },
        "message": "TUNIS",
        "msisdnArray": ["5318985507", "05393239896", "905455860993"],
        "originator": "TUNAHNCAKIL",
        "senddate": "",       
        "tags": ["deneme", "tayfun", "tunahan", "MERT"],
        "description": ""}
    x = requests.post(url, data = json.dumps(myobj))
    return HttpResponse('Sms gönderimi başarılı!')

class Anket(models.Model):
    id = models.AutoField(primary_key=True)
    anket_adi = models.CharField(max_length=100)
    anket_soru_id = models.ManyToManyField(Sorular)
    anket_isci_id = models.ManyToManyField(Isciler)
    mail_mesaj = models.TextField(max_length=500,null=True)
    subject = models.CharField(max_length=100,null=True)
    islem_tarihi = models.DateTimeField(auto_now_add=True)
    kullanici_adi = models.CharField(max_length=50,default=User)

    def __str__(self):
        return self.anket_adi