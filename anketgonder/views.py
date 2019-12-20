from anketgonder.models import Anket
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from anketgonder.forms import ContactForm

def email(request):
    if request.method == 'POST':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['info@ttyazilim.net'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('thanks')
    return render(request, "email.html", {'form': form})

def thanks(request):
    return HttpResponse('Thank you for your message.')


def smsgonder(request):
    return HttpResponse('Thank you for your message.') 