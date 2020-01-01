from django import forms
from anketgonder.models import Anket,Cevaplar

class AnketForm(forms.Form):

    def __init__(self, sorular, *args, **kwargs):
        super(AnketForm, self).__init__(*args, **kwargs)
        for soru in sorular:
            self.fields["%s" % soru] = forms.ChoiceField(required=True,widget=forms.RadioSelect(),choices=[('1','Çok Kötü'),('2','Kötü'),('3','Orta'),('4','İyi'),('5','Çok İyi')])