from django.shortcuts import render
from . import forms
from anket.models import Sorular
from anket.forms import AnketForm
from anketgonder.models import Anket

def index(request):
    return render(request,'anket-tema/index.html')

def head(request):
    return render(request,'anket-tema/iletisim.html')

def iletisim(request):
    Yazı = "Contact"
    return render(request,'anket-tema/iletisim.html',context=Yazı)

def base(request):
    return render(request,'anket-tema/base.html')

def anket_form_view(request):
    a = Anket.objects.get(id=4)                
    return render(request,'anket-tema/anket.html',{'sorularim' : a.anket_soru_id.all()})