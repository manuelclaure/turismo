from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.views.generic import ListView
from django.template import RequestContext
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import requires_csrf_token
from django.db.models import Q
from datetime import datetime
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
import requests
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.models import User
import json
from django.core.serializers.json import Serializer as JSONSerializer
from decimal import *
import datetime as dt
from django.http import HttpResponseRedirect
import base64
from .models import *
from administrador.models import *
from .forms import *
#from xhtml2pdf import pisa             # import python module
from rest_framework.views import APIView, Response
from django.views.generic.edit import CreateView
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse, Http404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def login(request):
    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        return render(request,"registro/menu.html")
    else:
        # Show an error page
        return render(request,"registration/login.html")

def cambiar_pass(request):
    form = UserCreationForm(data = request.POST)
    if request.method == 'POST':
       if form.is_valid:
          if request.POST['password1'] == request.POST['password2']:
             u = User.objects.get(username=request.POST.get('username', False))
             u.set_password(request.POST.get('password1', False))
             u.save()
             return render(request,"registro/menu.html")
          else:
              error  = "Passwords should match (typo?)"
              return render(request,"registration/cambiar_pass.html", {
        'form': form}, context_instance=RequestContext(request))
    else:
        form = UserCreationForm(initial={'username': request.user.username})
    return render(request,"registration/cambiar_pass.html", {
        'form': form}, context_instance=RequestContext(request))

def logout(request):
    logout(request)
    # Redirect to a success page.
    return render(request,"registration/logout.html")

def login_error(request):
    auth.logout(request)
    # Redirect to a success page.
    return render(request,"registration/login_error.html")

class TuristaCreateView(CreateView):
    model = Turista
    form_class = TuristaForm
    template_name = 'registro/turista.html'
    success_url = reverse_lazy('listar_turistas')
    permission_required = 'registro.add_turista'
    url_redirect = success_url    

    def get_form(self):
        form = super(TuristaCreateView, self).get_form()
        initial_base = self.get_initial() 
        return form

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                turista = Turista.objects.filter(documento=request.POST.get('documento','')).first()                
                if form.is_valid():
                   if self.request.user.groups.filter(name='Admin-Hotels').exists():  
                      hotel = Hotel.objects.filter(usuario__username=request.user.username).first()
                   if self.request.user.groups.filter(name='Operator-Hotels').exists():
                      usuariohotel=UsuarioHotel.objects.filter(usuario=self.request.user).first()
                      hotel=usuariohotel.hotel
                   if hotel:
                      if not turista: 
                         turista=form.save(commit=False) 
                         turista.save()
                      motivaciones = request.POST.getlist('motivacion[]')                      
                      turistahotel=TuristaHotel(turista=turista, hotel=hotel, fecha_ingreso=request.POST.get('fecha_ingreso',''), fecha_salida=request.POST.get('fecha_salida',''), procedencia=request.POST.get('fecha_salida','')) 
                      turistahotel.save()                     
                      for motivacion_id in motivaciones:
                          motivacion = Motivacion.objects.get(id=motivacion_id)
                          motivacionturista = MotivacionTurista(turistahotel=turistahotel, motivacion=motivacion)
                          motivacionturista.save()

                   return HttpResponseRedirect(self.url_redirect)
                else:
                    data['error'] = form.errors
            else:
                data['error'] = 'No ha ingresado a ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
    def get_context_data(self, **kwargs):
        context = super(TuristaCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Añadir turista'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        context['motivaciones'] = Motivacion.objects.all()
        return context

class TuristaListView(ListView):
    model = TuristaHotel
    template_name = 'registro/listarturistas.html'
    permission_required = 'registro.view_turista'
    url_redirect = reverse_lazy('index')

    def get_queryset(self):
        if self.request.user.groups.filter(name='Admin-Hotels').exists():
           hotel = Hotel.objects.get(usuario__username=self.request.user.username)
           return super(TuristaListView, self).get_queryset().filter(hotel=hotel)  
        else:
             if self.request.user.groups.filter(name='Operator-Hotels').exists():
                usuariohotel=UsuarioHotel.objects.filter(usuario=self.request.user).first()
                return super(TuristaListView, self).get_queryset().filter(hotel=usuariohotel.hotel)  

        return super(TuristaListView, self).get_queryset().all()  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'LISTADO DE TURISTAS'        
        context['action'] = 'searchdata'        
        context['create_url'] = reverse_lazy('crear_turista')
        context['list_url'] = reverse_lazy('listar_turistas')
        hotel=False  
        if self.request.user.groups.filter(name='Admin-Hotels').exists():  
           hotel = Hotel.objects.filter(usuario__username=self.request.user.username).first()
        if self.request.user.groups.filter(name='Operator-Hotels').exists():
           usuariohotel=UsuarioHotel.objects.filter(usuario=self.request.user).first()
           hotel=usuariohotel.hotel

        if hotel:
           context['nombre_hotel'] = hotel.nombre_hotel
        else: 
              context['nombre_hotel'] = 'NO TIENE ACCESO'

        return context

class TuristaUpdateView(UpdateView):
    model = TuristaHotel
    form_class = TuristaHotelForm
    template_name = 'registro/change_turista.html'
    success_url = reverse_lazy('listar_turistas')
    permission_required = 'registro.change_turista'
    url_redirect = success_url    
    

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                turistahotel=TuristaHotel.objects.get(id=self.kwargs['pk'])
                form = self.get_form()                
                if form.is_valid():  
                   motivaciones = request.POST.getlist('motivacion[]')                                         
                   turistahotel1=form.save(commit=False)                     
                   turistahotel.fecha_ingreso=turistahotel1.fecha_ingreso
                   turistahotel.save()
                   for motivacion_id in motivaciones:

                       motivacion = Motivacion.objects.get(id=motivacion_id)
                       motivacionturista = MotivacionTurista(turistahotel=turistahotel, motivacion=motivacion)
                       motivacionturista.save()

                   return HttpResponseRedirect(self.url_redirect)
                else:
                    data['error'] = form.errors
            else:
                data['error'] = 'No ha ingresado a ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
    def get_context_data(self, **kwargs):
        context = super(TuristaUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Añadir turista'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        motivaciones = Motivacion.objects.all() 
        motivaciones1 = []
        for motivacion in motivaciones:            
            if MotivacionTurista.objects.filter(turistahotel=self.kwargs['pk'], motivacion=motivacion):
               motiv = {
                  'id':motivacion.id,
                  'nombre_motivacion':motivacion.nombre_motivacion,
                  'estado':'True'
                  }
            else:
                motiv = {
                  'id':motivacion.id,
                  'nombre_motivacion':motivacion.nombre_motivacion,
                  'estado':'False'
                  }
            motivaciones1.append(motiv)
        context['motivaciones'] = motivaciones1        
        return context

class TuristaDeleteView(DeleteView):
    model = TuristaHotel
    form_class = TuristaHotelForm
    template_name = 'registro/change_turista.html'
    success_url = reverse_lazy('listar_turistas')
    permission_required = 'registro.change_turista'
    url_redirect = success_url        
    
    def get_context_data(self, **kwargs):
        context = super(TuristaDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Eliminar turista'
        context['list_url'] = self.success_url
        context['action'] = 'add'        
        return context