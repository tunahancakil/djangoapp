from django.shortcuts import render
from anketgonder.models import Anket

def anket_gonder(request):
    return render(request,'index.html')