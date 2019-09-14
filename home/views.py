from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect, Http404
from django.contrib.auth.models import User
from django.contrib import messages
from anket.models import Sorular
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from anket.soruform import SorularForm

# Create your views here.
def home_view(request):
    sorularım = Sorular.objects.all()
    soruform = SorularForm()
    if request.user.is_authenticated:
        context = {
            'isim' : 'Tuna',
            'soru_baslik' : soruform,
            'sorularim' : sorularım,
        }
    else:
        context = {
            'isim' : 'Misafir'
        }
    return render(request, 'index.html',context)
