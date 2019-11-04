from django import forms
from .models import *

class SorularForm(forms.ModelForm):

    class Meta:
        model = Sorular,UyeKurumlar
        fields = [
            'soru_baslik',
            'soru_icerik',
            'cevap',
        ]