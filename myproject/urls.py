"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapi.views import getsku, norder, getorders, deleteall, getuser, deleteid, redactid, newuser, getordersweb, \
    addform, add,website,redactbyid,getskutable,add_drink_form,signin,signinform,profile,testadmin
urlpatterns = [
    path("", website, name="website"),
    path('admin/', admin.site.urls),
    path('myadmin/', testadmin),
    path('api/getsku/',getsku),
    path('api/getskutable/',getskutable),
    path('api/redactbyid/',redactbyid),
    path('api/norder/',norder),
    path('api/getorders/',getorders),
    path('api/getordersweb/',getordersweb),
    path('api/deleteall/',deleteall),
    path('api/deleteid/', deleteid),
    path('api/redactid/', redactid),
    path('api/getuser/', getuser),
    path('api/signin/', signin),
    path('api/newuser/', newuser),
    path('manager/add/', add),
    path('profile', profile),
    path("manager/addform/", addform, name="addform"),
    path("manager/adddrink/", add_drink_form, name="add_drink_form"),
    path("invite/", website, name="website"),
    path("signinform/", signinform, name="signinform"),

              ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
