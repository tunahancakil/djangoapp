from django.shortcuts import render,redirect
from anket.models import Sorular,Isciler
from anket.forms import AnketForm
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
    if request.method == "POST":
        key = 'secret'
        decoded = jwt.decode(encoded, key, 'utf-8') 
        a = Anket.objects.get(id=decoded['isci_id'])
        form_ = AnketForm(request.POST)
        print(request.POST)
        print("here1")
        if form_.is_valid():
            newLabel = form_.save()

            return redirect("index")
        context = {
            "form" : form_
        }
        return render(request,"anket-tema/anket.html",context)
    else:
        form_ = AnketForm()
        context = {
            "form" : form_
        }
        return render(request,"anket-tema/anket.html",context)
"""
if request.method == 'POST':
        print('here')
        form_ = AnketForm(request.POST)
        print(str(request.Post))
    
        if form_.is_valid():
            print('here2')
            print(form_.cleaned_data['Soru'])
            AnketForm.save()
            return HttpResponseRedirect('/thanks')
    else:
        key = 'secret'
        print(encoded)
        decoded = jwt.decode(encoded, key, 'utf-8') 
        print(decoded)
        a = Anket.objects.get(id=decoded['isci_id'])
        form = AnketForm(a.anket_soru_id.all())
        return render(request,'anket-tema/anket.html',{'form':form})
  """