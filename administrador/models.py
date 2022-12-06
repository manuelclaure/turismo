from django.db import models
from django.contrib.auth.models import User
# Create your models here.
ESTADO_CHOICES = (
    ('ACTIVO', 'ACTIVO'),
    ('INACTIVO', 'INACTIVO'),
)

class Provincia(models.Model):
    nombre_provincia = models.CharField(max_length=25)
    def __str__(self):
        return '{}'.format(self.nombre_provincia)


class Municipio(models.Model):
    nombre_municipio = models.CharField(max_length=25)
    provincia=models.ForeignKey(Provincia, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.nombre_municipio)    


class Hotel(models.Model):
    nombre_hotel = models.CharField(max_length=25)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=25)    
    usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    estado = models.CharField(max_length=15, choices=ESTADO_CHOICES)
    municipio = models.ForeignKey(Municipio, null=True, blank=True, on_delete=models.CASCADE)
    celular = models.CharField(max_length=25, null=True, blank=True)
    eslogan = models.CharField(max_length=35, null=True, blank=True)
    logo = models.ImageField(upload_to="uploads/shows", null=True, blank=True)  
    estrellas = models.IntegerField(null=True, blank=True)   

class UsuarioHotel(models.Model):
    usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, null=True, blank=True, on_delete=models.CASCADE)

class Config(models.Model):
    directorio = models.CharField(max_length=225)

    
