from django.shortcuts import render
from . import forms
from anket.models import Sorular
from anket.forms import AnketForm

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
    form = AnketForm()
    sorularim = Sorular.objects.all()
    if request.method == "POST":
        form = AnketForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print ('Hata form geçerli bilgiler içermiyor.')
    return render(request,'anket-tema/anket.html',{'form':form,'sorularim' : sorularim})