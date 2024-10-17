"""
URL configuration for cv_generator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from .views import userForm, submitform,generatePDF,list_of_all_users, showdetails
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('userform/', userForm, name='userform'),
    path('submitform/', submitform, name='submitform'),
    path('showdetails/int:<id>/', showdetails, name='showdetails'),
 
    path('listofusers/',list_of_all_users,name='listofusers'),
    path('generatepdf/', generatePDF, name='generatepdf'),    
     
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
