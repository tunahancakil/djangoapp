from django import forms
import json
import requests

class ContactForm(forms.Form):

    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea)
    url = 'http://sms.corvass.net/jsona'
    myobj = {"Authentication": {           
             "apikey": "4775500361",           
             "apisecret": "0n6hu04dyiz23xyh9m6m"       },
             "message": "TUNIS",
             "msisdnArray": ["5318985507", "05393239896", "905455860993"],
             "originator": "TUNAHNCAKIL",
             "senddate": "",       
             "tags": ["deneme", "tayfun", "tunahan", "MERT"],
             "description": ""}
    x = requests.post(url, data = json.dumps(myobj))
   