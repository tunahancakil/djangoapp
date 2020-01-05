from django import forms
from django.forms import ModelForm
from anketgonder.models import Sorular,Cevaplar
import jwt


class AnketForm(forms.Form):
    deger = forms.IntegerField(widget=forms.Select(choices=Cevaplar.DEGER_CHOICES))
    anket_isci_id = forms.IntegerField()
    #anket_soru_id[] = forms.IntegerField()
    print("hereanket")    
    def __init__(self, sorular, *args, **kwargs):
        super(AnketForm, self).__init__(*args, **kwargs)
        for soru in sorular:
            pass
            #self.fields["%s" % soru] = forms.ChoiceField(required=True,widget=forms.RadioSelect(),choices=[('1','Çok Kötü'),('2','Kötü'),('3','Orta'),('4','İyi'),('5','Çok İyi')])


    #def clean(self):
     #   deger1 = self.cleaned_data.get("deger1")
        #anket_soru_id = self.cleaned_data.get("anket_soru_id")

      #  values = {
       #     "deger" : deger1,
            #"anket_soru_id" : anket_soru_id,
       # }
        #return values
        #self.sorular = sorular
        #for soru in sorular:
        #    self.fields["%s" % soru] = forms.ChoiceField(required=True,widget=forms.RadioSelect(),choices=[('1','Çok Kötü'),('2','Kötü'),('3','Orta'),('4','İyi'),('5','Çok İyi')])
        #def __init__(self, sorular, *args, **kwargs):
        #super(AnketForm, self).__init__(*args, **kwargs)

class AnketForm(ModelForm):
    class Meta:
        model = Cevaplar
        fields = ['deger','anket_isci_id',]
        widgets = {'anket_isci_id': forms.HiddenInput()}