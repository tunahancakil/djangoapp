from django.shortcuts import render
from . import forms
from anket.models import Sorular
from anket.forms import AnketForm
from anketgonder.models import Anket,Cevaplar

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
        # create a form instance and populate it with data from the request:
        form = AnketForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            print(form.cleaned_data['Soru'])
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        key = 'secret'
        decoded = jwt.decode(encoded, key, 'utf-8') 
        a = Anket.objects.get(id=decoded['isci_id'])
        form = AnketForm(a.anket_soru_id.all())
        return render(request,'anket-tema/anket.html',{'form':form})
  