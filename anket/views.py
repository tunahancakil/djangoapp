from django.shortcuts import render
from . import forms
from anket.models import Sorular
from anket.forms import AnketForm

# Create your views here.
def index(request):
    return_deger = {'x':'Hello world!!! this is view.py'}
    return render(request,'index.html', context= return_deger)

def anket_form_view(request):
    form = AnketForm()
    sorularim = Sorular.objects.all()

    if request.method == "POST":
        form = AnketForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print ('Error form geçerli bilgiler içermiyor.')

    return render(request,'form.html',{'form':form,'sorularim' : sorularim})