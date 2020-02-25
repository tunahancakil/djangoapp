from django.contrib import admin
from django.template import loader
from django.utils.html import format_html
from django.shortcuts import render,redirect
from django.core.mail import send_mail
from anketgonder.models import *
from django.urls import reverse,path
from django.http import HttpResponse
from django import forms
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from  bitly_api import bitly_api
import smtplib
import sys
import json
import requests
import urllib
import jwt
import csv, io

class CsvImportForm(forms.Form):
    csv_file = forms.FileField()

@admin.register(Kurumlar)
class KurumlarAdmin(admin.ModelAdmin):
    list_display  = ['unvan', 'email','islem_tarihi']
    list_filter = ['islem_tarihi']
    list_display_links = ('unvan', 'email')
    search_fields = ['unvan']
    list_per_page = (10)

@admin.register(Sorular)
class SorularAdmin(admin.ModelAdmin):
    list_display = ['id','soru_baslik','soru_icerik','islem_tarihi']

@admin.register(Yoneticiler)
class YoneticilerAdmin(admin.ModelAdmin):
    list_display = ['ad','soyad','kurum',]

@admin.register(Isciler)
class IscilerAdmin(admin.ModelAdmin):
    list_display  = ['ad','soyad','email','iletisim_no']
    list_filter = ['islem_tarihi']

    change_list_template = "anket-tema/excel-upload.html"    

    def  get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('import-csv/', self.import_csv),
        ]
        return custom_urls + urls   

    def import_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_file"]
            data_set = csv_file.read().decode('UTF-8')
            io_string = io.StringIO(data_set)
            for column in csv.reader(io_string, delimiter=',', quotechar="|"):
                _, created = Isciler.objects.update_or_create(
                    ad=column[0],
                    soyad=column[1],
                    email=column[2],
                    iletisim_no=column[3],
                    yonetici=Yoneticiler.objects.get(id=column[4])
                )
            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(request, "anket-tema/csv_form.html", payload)    
