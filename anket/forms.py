from django import forms
from django.forms import ModelForm
from anketgonder.models import Sorular,Cevaplar
import jwt

class AnketForm(forms.Form):
    def __init__(self, sorular, *args, **kwargs):
        super(AnketForm, self).__init__(*args, **kwargs)
    deger = forms.IntegerField(widget=forms.Select(choices=Cevaplar.DEGER_CHOICES))
    sorular = forms.CharField(max_length=200)
    anket_isci_id = forms.IntegerField()
    anket_soru_id = forms.IntegerField()

    def clean(self):
        deger1 = self.cleaned_data.get("deger1")
        anket_isci_id = self.cleaned_data.get("anket_isci_id")
        anket_soru_id = self.cleaned_data.get("anket_soru_id")

        values = {
            "deger" : deger1,
            "anket_isci_id" : anket_isci_id,
            "anket_soru_id" : anket_soru_id,
        }
        return values
        #self.sorular = sorular
        #for soru in sorular:
        #    self.fields["%s" % soru] = forms.ChoiceField(required=True,widget=forms.RadioSelect(),choices=[('1','Çok Kötü'),('2','Kötü'),('3','Orta'),('4','İyi'),('5','Çok İyi')])
        #def __init__(self, sorular, *args, **kwargs):
        #super(AnketForm, self).__init__(*args, **kwargs)

class AnketForm(ModelForm):
    class Meta:
        model = Cevaplar
        fields = ['deger','anket_isci_id','anket_soru_id',]
        #widgets = {'anket_isci_id': forms.HiddenInput(),'anket_soru_id': forms.HiddenInput()}