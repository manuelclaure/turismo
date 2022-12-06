from django.contrib import admin
from django.urls import path
from . import views
from .views import *
from django.conf.urls import include
from . import views
#from django.conf.urls import url
from django.views.static import serve
from django.contrib.auth.decorators import login_required,permission_required
from django.conf.urls.static import static
urlpatterns = [
    path('hotel',   permission_required('administrador.add_hotel')(views.HotelCreateView.as_view()), name='crear_hotel'),    
    path('hoteles',  permission_required('administrador.view_hotel')(views.HotelListView.as_view()), name='listar_hoteles'), 
    path('change_hotel/<pk>/',  permission_required('auth.change_hotel')(views.HotelUpdateView.as_view()), name='change_hotel'),    
    path('delete_hotel/<pk>/',  permission_required('auth.delete_hotel')(views.HotelDeleteView.as_view()), name='delete_hotel'),    
    path('usuario',  permission_required('auth.add_user')(views.UsuarioCreateView.as_view()), name='crear_usuario'),       
    path('usuarios',  permission_required('auth.view_user')(views.UsuarioListView.as_view()), name='listar_usuarios'),
    path('change_user/<pk>/',  permission_required('auth.change_user')(views.ModificarUsuarioView.as_view()), name='change_user'),    
    path('delete_user/<pk>/',  permission_required('auth.delete_user')(views.EliminarUsuarioView.as_view()), name='delete_usuario'),    
    path('reportes',  permission_required('administrador.view_reportes')(views.reportes), name='reportes'),    
]