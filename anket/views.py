from django.shortcuts import render
from . import forms
from anket.models import Sorular
from anket.forms import AnketForm
from anketgonder.models import Anket,Cevaplar
from django.http import HttpResponse, HttpResponseRedirect
import jwt

def index(request):
    return render(request,'anket-tema/index.html')

def head(request):
    return render(request,'anket-tema/iletisim.html')

def iletisim(request):
    Yazı = "Contact"
    return render(request,'anket-tema/iletisim.html',context=Yazı)

def base(request):
    return render(request,'anket-tema/base.html')

def anket_form_view(request,encoded):
    
    if request.method == 'POST':
        print('here')
        form = AnketForm(request.POST)
        #Cevaplar.deger = form.fields
        
        print(form.fields.values)
        if form.is_valid():
            print(form.cleaned_data['Soru'])
            AnketForm.save()
        return HttpResponseRedirect('/thanks')
    else:
        key = 'secret'
        decoded = jwt.decode(encoded, key, 'utf-8') 
        a = Anket.objects.get(id=decoded['isci_id'])
        form = AnketForm(a.anket_soru_id.all())
        return render(request,'anket-tema/anket.html',{'form':form})
  