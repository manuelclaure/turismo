from django.contrib import admin
from django.urls import path
from . import views
from .views import *
from django.conf.urls import include
from . import views
from django.urls import re_path
from django.views.static import serve
from django.contrib.auth.decorators import login_required,permission_required
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #url(r'^accounts/', include('registration.backends.simple.urls')),
    re_path(r'^admin/', admin.site.urls),
    path('accounts/login',  views.login),
    path('logout',  views.logout),
    path('turista',  permission_required('registro.add_turista')(views.TuristaCreateView.as_view()), name='crear_turista'),    
    path('turistas',  permission_required('registro.view_turista')(views.TuristaListView.as_view()), name='listar_turistas'),  
    path('change_turista/<pk>/',  permission_required('registro.change_turista')(views.TuristaUpdateView.as_view()), name='change_turista'),    
    path('delete_turista/<pk>/',  permission_required('registro.delete_turista')(views.TuristaDeleteView.as_view()), name='delete_turista'),          
]