from django import forms
import json
import requests
from django.utils.html import format_html
from .models import *
from anket.models import *

class ContactForm(forms.Form):

    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea)
   