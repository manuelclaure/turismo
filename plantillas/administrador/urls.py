from django.contrib import admin
from django.urls import path
from . import views
from .views import *
from django.conf.urls import include
from . import views
from django.conf.urls import url
from django.views.static import serve
from django.contrib.auth.decorators import login_required,permission_required
urlpatterns = [
    path('hotel',  views.HotelCreateView.as_view(), name='crear_hotel'),    
    path('hoteles',  views.HotelListView.as_view(), name='listar_hoteles'),    
]