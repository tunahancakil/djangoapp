from django.shortcuts import render,redirect
from anket.models import Sorular,Isciler
from anket.forms import AnketForm,AnketModelForm
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
    a = Anket.objects.get(id=decoded['isci_id'])
    anket_sorulari_id = a.anket_soru_id.all()
    if request.method == "POST":
        form_ = AnketForm(request.POST)
        if form_.is_valid():
            print("here-save")
            for soru in anket_sorulari_id :
                print('soru')
                print(str(soru.id))
                print("cevap")
                print(request.POST.get(str(soru.id),False))
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
        print("here2")
        #print(a.id)
        #sorular = a.anket_soru_id.all()
        form_ = AnketForm(anket=a)
        #print(AnketForm)
       # for e in sorular:
        #    print(e)
         #   pass
            #initial={'anket_isci_id':a.id,'anket_sorular':sorular}
        context = {
            "form" : form_,
            "prueba" : "var ty = document.getElementById(1)"        
        }
        return render(request,"anket-tema/anket.html",context=context)
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