from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from anket.models import Sorular

# Create your views here.

def home_view(request):
    if request.user.is_authenticated:
        context = {
            'isim' : 'Tuna'
        }
    else:
        context = {
            'isim' : 'Misafir'
        }
    return render(request, 'index.html',context)