from django.shortcuts import render
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

from registro.models import Turista
from .models import *
from .forms import *
from .reportes import *
from rest_framework.views import APIView, Response
from django.views.generic.edit import CreateView
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse, Http404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import Group

# Create your views here.
class HotelListView(ListView):
    model = Hotel
    template_name = 'administrador/listarhoteles.html'
    permission_required = 'administrador.view_hotel'
    url_redirect = reverse_lazy('index')

    def get_queryset(self):
        return super(HotelListView, self).get_queryset().all()  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'LISTADO DE HOTELES'        
        context['action'] = 'searchdata'        
        context['create_url'] = reverse_lazy('crear_hotel')
        context['list_url'] = reverse_lazy('listar_hoteles')        

        return context

class HotelCreateView(CreateView):
    model = Hotel
    form_class = HotelForm
    template_name = 'administrador/hotel.html'
    success_url = reverse_lazy('listar_hoteles')
    permission_required = 'administrador.add_hotel'
    url_redirect = success_url    

    def get_form(self):
        form = super(HotelCreateView, self).get_form()
        initial_base = self.get_initial() 
        return form

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                if form.is_valid():
                    hotel=form.save(commit=False)
                    usuario=User(username=request.POST.get('usuario',''))
                    usuario.set_password(request.POST.get('usuario',''))
                    usuario.save()
                    hotel.usuario=usuario
                    hotel.save()
                    group=Group.objects.get(name='Admin-Hotels')
                    group.user_set.add(usuario)
                    return HttpResponseRedirect(self.url_redirect)
                else:
                    data['error'] = form.errors
            else:
                data['error'] = 'No ha ingresado a ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
    def get_context_data(self, **kwargs):
        context = super(HotelCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Añadir hoteles'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context

class HotelUpdateView(UpdateView):
    model = Hotel
    form_class = HotelForm
    template_name = 'administrador/hotel.html'
    success_url = reverse_lazy('listar_hoteles')
    permission_required = 'administrador.add_hotel'
    url_redirect = success_url    

    def get_form(self):
        form = super(HotelUpdateView, self).get_form()
        initial_base = self.get_initial() 
        return form

    def get_context_data(self, **kwargs):
        context = super(HotelUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Modificar hoteles'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        context['usuario'] = 'add'
        context['estrellas'] = 'add'
        return context

class HotelDeleteView(DeleteView):
    model = Hotel
    form_class = HotelForm
    template_name = 'administrador/hotel.html'
    success_url = reverse_lazy('listar_hoteles')
    permission_required = 'auth.delete_hotel'
    url_redirect = success_url   
 
    def get_context_data(self, **kwargs):
        context = super(HotelDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Eliminar hotel'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context

class UsuarioListView(ListView):
    model = UsuarioHotel
    template_name = 'administrador/listarusuarios.html'
    permission_required = 'auth.view_user'
    url_redirect = reverse_lazy('index')

    def get_queryset(self):
        if self.request.user.is_superuser:
            print("Administrador")
            return super(UsuarioListView, self).get_queryset().all()              
        else:
             if self.request.user.groups.filter(name='Admin-Hotels').exists():   
                print("Administrador de hoteles")                               
                hotel=Hotel.objects.filter(usuario=self.request.user).first()                 
                return super(UsuarioListView, self).get_queryset().filter(hotel=hotel)  
             else:
                 print(self.request.user.id)
                 return super(UsuarioListView, self).get_queryset().filter(id=0)  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'LISTADO DE USUARIOS'        
        hotel=Hotel.objects.filter(usuario=self.request.user).first()        
        if hotel:
           context['nombre_hotel'] = hotel.nombre_hotel
        else:
            context['nombre_hotel'] = 'Administrador'
        context['action'] = 'searchdata'        
        context['create_url'] = reverse_lazy('crear_usuario')
        context['list_url'] = reverse_lazy('listar_usuarios')        

        return context

class UsuarioCreateView(CreateView):
    model = User
    form_class = UsuarioForm
    template_name = 'administrador/usuario.html'
    success_url = reverse_lazy('listar_usuarios')
    permission_required = 'auth.add_user'
    url_redirect = success_url    

    def get_form(self):
        form = super(UsuarioCreateView, self).get_form()
        initial_base = self.get_initial() 
        return form

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                if form.is_valid():
                    usuario=form.save(commit=False)
                    usuario.set_password(usuario.username)
                    usuario.save()                    
                    group=Group.objects.get(name='Operator-Hotels')
                    group.user_set.add(usuario)
                    hotel=Hotel.objects.filter(usuario=request.user).first()
                    usuariohotel=UsuarioHotel(usuario=usuario, hotel=hotel)
                    usuariohotel.save()

                    return HttpResponseRedirect(self.url_redirect)
                else:
                    data['error'] = form.errors
            else:
                data['error'] = 'No ha ingresado a ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
    def get_context_data(self, **kwargs):
        context = super(UsuarioCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Añadir usuarios'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context

class ModificarUsuarioView(UpdateView):
    model = User
    form_class = UsuarioForm3
    template_name = 'administrador/usuario.html'
    success_url = '/administrador/usuarios'
    permission_required = 'auth.change_user'
    url_redirect = success_url       

    def get_context_data(self, **kwargs):
        context = super(ModificarUsuarioView, self).get_context_data(**kwargs)
        context['title'] = 'Modificar usuario'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context

class EliminarUsuarioView(DeleteView):
    model = User
    form_class = UsuarioForm3
    template_name = 'administrador/usuario.html'
    success_url = '/administrador/usuarios'
    permission_required = 'auth.delete_user'
    url_redirect = success_url   
 
    def get_context_data(self, **kwargs):
        context = super(EliminarUsuarioView, self).get_context_data(**kwargs)
        context['title'] = 'Eliminar usuario'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context

def reportes(request):
    # Redirect to a success page.
    if request.user.is_superuser:
       hoteles = Hotel.objects.all()
    else:
        if request.user.groups.filter(name='Admin-Hotels').exists():
           hoteles=Hotel.objects.filter(usuario=request.user)
        if request.user.groups.filter(name='Operator-Hotels').exists():
           usuariohotel=UsuarioHotel.objects.filter(usuario=request.user).first()
           hoteles=Hotel.objects.filter(id=usuariohotel.hotel.id)

    if request.method == 'POST':
       opcion = request.POST.get('opcion','')
       if opcion=='1': 
          turista=Turista.objects.all()
          xfecha_inicial=request.POST.get('fecha_inicial','')       
          xfecha_final=request.POST.get('fecha_final','')
          xid_hotel=request.POST.get('id_hotel','')
          report=ReporteListaTuristas(turista, xfecha_inicial, xfecha_final, xid_hotel)
       if opcion=='2': 
          turista=Turista.objects.all()
          xfecha_inicial=request.POST.get('fecha_inicial','')       
          xid_hotel=request.POST.get('id_hotel','')
          print(xfecha_inicial)
          print(xid_hotel)
          report=ReportePartesHoteleras(turista, xfecha_inicial, xid_hotel)
       return report.render_to_response()
    
    return render(request,"administrador/reportes.html", {'hoteles':hoteles })