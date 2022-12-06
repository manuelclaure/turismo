from django.db import models
from django.contrib.auth.models import User
from administrador.models import Hotel
# Create your models here.
GENERO_CHOICES = (
    ('MASCULINO', 'MASCULINO'),
    ('FEMENINO', 'FEMENINO'),
    ('OTRO', 'OTRO'),
)
MODALIDAD_CHOICES = (
    ('INDIVIDUAL', 'INDIVIDUAL'),
    ('GRUPO', 'GRUPO'),
)
ESTADO_CHOICES = (
    ('ACTIVO', 'ACTIVO'),
    ('INACTIVO', 'INACTIVO'),
)
ESTADOCIVIL_CHOICES = (
    ('SOLTERO(A)', 'SOLTERO(A)'),
    ('CASADO(A)', 'CASADO(A)'),
    ('VIUDO(A)', 'VIUDO(A)'),
    ('DIVORCIADO(A)', 'DIVORCIADO(A)'),
)
class Continente(models.Model):
    nombre_continente = models.CharField(max_length=25)
    def __str__(self):
        return '{}'.format(self.nombre_continente)

class Motivacion(models.Model):
    nombre_motivacion = models.CharField(max_length=25)
    def __str__(self):
        return '{}'.format(self.nombre_motivacion)

class Pais(models.Model):
    nombre_pais = models.CharField(max_length=45)
    continente = models.ForeignKey(Continente, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.nombre_pais)

class TipoDocumento(models.Model):
    tipodocumento = models.CharField(max_length=25)
    estado = models.CharField(max_length=10)
    def __str__(self):
        return '{}'.format(self.tipodocumento)

class Turista(models.Model):
    documento = models.CharField(max_length=25)
    tipodocumento = models.ForeignKey(TipoDocumento, null=True, blank=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=25)
    a_paterno = models.CharField(max_length=25)
    a_materno = models.CharField(max_length=25)
    genero = models.CharField(max_length=25, choices=GENERO_CHOICES)
    edad = models.IntegerField()
    profesion = models.CharField(max_length=125)
    nacionalidad = models.ForeignKey(Pais, null=True, blank=True, on_delete=models.CASCADE)
    modalidad_viaje = models.CharField(max_length=15, choices=MODALIDAD_CHOICES)    
    duracion_estadia = models.IntegerField()
    gasto_diario = models.FloatField()
    observaciones = models.CharField(max_length=125)
    estado_civil = models.CharField(max_length=50, choices=ESTADOCIVIL_CHOICES, null=True, blank=True)
    expedido = models.CharField(max_length=35, null=True, blank=True)
    def __str__(self):
        return '{}'.format(self.nombre + ' ' + self.a_paterno + ' ' +self.a_materno)

class TuristaHotel(models.Model):
    turista = models.ForeignKey(Turista, null=True, blank=True, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, null=True, blank=True, on_delete=models.CASCADE)
    fecha_ingreso = models.DateField()
    fecha_salida = models.DateField()
    procedencia = models.CharField(max_length=125, null=True, blank=True)
    def __str__(self):
        return '{}'.format(self.id)

class MotivacionTurista(models.Model):
    motivacion = models.ForeignKey(Motivacion, null=True, blank=True, on_delete=models.CASCADE)
    turistahotel = models.ForeignKey(TuristaHotel, null=True, blank=True, on_delete=models.CASCADE)



    