from django import forms
from django.forms import ModelForm,ChoiceField,Field
from anketgonder.models import Sorular,Cevaplar
import jwt

class AnketForm(forms.Form):
    choices=Cevaplar.DEGER_CHOICES
    #anket_isci_id = forms.IntegerField()
    #anket_soru_icerik = forms.CharField()

    def __init__(self, *args, **kwargs):
       # if 'errormessage' in kwargs:
        #    print("yeah it's here")
        try:
            self.anket = kwargs.pop('anket')
        except:
            pass  
        super(AnketForm, self).__init__(*args, **kwargs)
        #print('here3')
        #i = 0
        #for soru in self.anket.anket_soru_id.all():
            #print(soru)
            #self.fields['soru_%s' % (i+1,)] = forms.CharField(initial=soru.soru_icerik)
            #self.fields['deger_%s' % (i+1,)] = forms.IntegerField(widget=forms.Select(choices=Cevaplar.DEGER_CHOICES))
        #    i+=1

              #  for i in range(len(self.anket.anket_soru_id.all())):
       #     field_name = 'soru_%s' % (i+1,)
        #    self.fields[field_name] = forms.IntegerField(self.anket.anket_soru_id.all().get(i))
    
    def clean(self):
        deger1 = self.cleaned_data.get("deger1")

        values = {
            "deger" : deger1,
        }
        return values

class AnketModelForm(ModelForm):
    class Meta:
        model = Cevaplar
        fields = ['deger','anket_isci_id','anket_soru_id']
        #widgets = {'anket_isci_id': forms.HiddenInput(),}