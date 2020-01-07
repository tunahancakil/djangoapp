from django.shortcuts import render,redirect
from anket.models import Sorular,Isciler
from anket.forms import AnketForm
from anket.soruform import SorularForm
from anketgonder.models import Anket,Cevaplar
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
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
    key = 'secret'
    decoded = jwt.decode(encoded, key, 'utf-8') 
    a = Anket.objects.get(id=decoded['anket_id'])
    anket_sorulari_id = a.anket_soru_id.all()
    if request.method == "POST":
        form_ = AnketForm(request.POST)
        if form_.is_valid():
            for soru in anket_sorulari_id :
                c = Cevaplar.objects.create(
                    deger = request.POST.get(str(soru.id),False),    
                    anket_soru_id = Sorular.objects.filter(id=str(soru.id))[0],    
                    anket_isci_id = Isciler.objects.filter(id=decoded['isci_id'])[0])
                kaydet = c.save()
            return redirect("index")
        context = {
            "form" : form_
           
        }
        return render(request,"anket-tema/anket.html",context)
    else:
        form_ = AnketForm(anket=a)
        context = {
            "form" : form_     
        }
        return render(request,"anket-tema/anket.html",context=context)