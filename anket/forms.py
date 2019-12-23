from django import forms
from django.forms import ModelForm
from anket.models import Sorular

class AnketForm(forms.ModelForm):
    class Meta():
        model = Sorular
        fields = ('soru_icerik',)