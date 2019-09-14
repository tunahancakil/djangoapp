from django import forms
from .models import Sorular

class SorularForm(forms.ModelForm):

    class Meta:
        model = Sorular
        fields = [
            'soru_baslik',
            'soru_icerik',
            'cevap',
        ]