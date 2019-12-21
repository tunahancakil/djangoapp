from anketgonder.models import Anket
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from anketgonder.forms import ContactForm

def thanks(request):
    return HttpResponse('Thank you for your message.')


def smsgonder(request):
    return HttpResponse('Thank you for your message.') 