"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home.views import home_view
from anket.views import *
from anketgonder.views import *

admin.site.site_header = "TT Yazılım Admin Panel"
admin.site.site_title = "TT Yazılım Admin Portal"
admin.site.index_title = "TT Yazılım Admin Portala Hoşgeldiniz"

urlpatterns = [
    path('',index,name='index'),
    path('iletisim',contact,name='iletisim'),
    path('makale',article,name='makale'),
    #path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('tema/anket/<str:encoded>',anket_form_view, name='anket_form'),
    path('thanks', thanks, name='thanks'),
]
