from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect, Http404
from django.contrib.auth.models import User
from django.contrib import messages
from anket.models import Sorular
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def home_view(request):
    sorularım = Sorular.objects.all()
    if request.user.is_authenticated:
        context = {
            'isim' : 'Tuna',
            'sorularim' : sorularım,
        }
    else:
        context = {
            'isim' : 'Misafir'
        }
    return render(request, 'index.html',context)
