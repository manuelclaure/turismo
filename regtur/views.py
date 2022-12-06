from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404,render,HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.forms import AdminPasswordChangeForm, AuthenticationForm, authenticate, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
#from django.core.urlresolvers import reverse
from django.urls import reverse
from django.forms import ModelForm
from django.views.decorators import *
from django.contrib.sessions.models import Session
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core import serializers
from datetime import datetime
from django.contrib.auth.models import auth
import json
import os
import time
# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def index(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/privado')
    else:
        return HttpResponseRedirect('/login/')
@login_required
def privado(request):
    if request.user.is_authenticated:
       usuario=request.user
       if usuario.is_active:
          if usuario.is_superuser:
             return render(request,"registro/menu.html")
          else:
               return render(request,"registro/menu2.html")			
       else:
           return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
       

def login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
    #    # Correct password, and the user is marked "active"
        auth.login(request, user)
    #    # Redirect to a success page.
        if user.is_superuser:
           return render(request,"registro/menu.html")
        else:
             return render(request,"registro/menu2.html")
    #else:
    #    # Show an error page
    print("prueba")
    return render(request,"registration/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login')