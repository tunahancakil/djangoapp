from django.core.mail import send_mail

send_mail(
    'Subject here',
    'Here is the message.',
    'tunahancakil@gmail.com',
    ['info@ttyazilim.net'],
    fail_silently=False,
)