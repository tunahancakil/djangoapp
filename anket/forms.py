from django import forms
from django.forms import ModelForm,ChoiceField,Field
from anketgonder.models import Sorular,Cevaplar
import jwt

class AnketForm(forms.Form):
    choices=Cevaplar.DEGER_CHOICES

    def __init__(self,  *args, **kwargs):
        try:
            self.anket = kwargs.pop('anket')
        except:
            pass  
        super(AnketForm, self).__init__(*args, **kwargs)
        