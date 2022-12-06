from django.forms import *
from .models import *

class TuristaForm(ModelForm):
    class Meta:
        model = Turista
        fields = ['documento', 'expedido', 'tipodocumento', 'nombre', 'a_paterno', 'a_materno', 'genero', 'edad',  'profesion', 'modalidad_viaje','duracion_estadia',  'gasto_diario', 'observaciones', 'estado_civil', 'nacionalidad']
        labels = {
            'documento': ('Documento de identidad'), 
            'expedido': ('Expedido'),
            'tipodocumento': ('Tipo de documento'), 
            'nombre': ('Nombre'), 
            'a_paterno': ('Apellido Paterno'), 
            'a_materno': ('Apellido Materno'), 
            'genero': ('Genero'), 
            'edad': ('Edad'),  
            'profesion': ('Profesion'), 
            'nacionalidad': ('Nacionalidad'), 
            'estado_civil': ('Estado Civil'), 
            'modalidad_viaje': ('Modalidad'), 
            'duracion_estadia': ('Duracion de la estadia'),  
            'gasto_diario': ('Gasto diario (BOB.)'), 
            'observaciones': ('Observaciones'),            
        }
        #widgets = {'mes': TextInput(attrs={'readonly': 'readonly'}), 'gestion': TextInput(attrs={'readonly': 'readonly'})}
        exclude = []
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'    

class TuristaHotelForm(ModelForm):
    class Meta:
        model = TuristaHotel
        fields = ['turista', 'fecha_ingreso', 'fecha_salida', 'procedencia']
        labels = {
            'fecha_ingreso' : ('Fecha Ingreso'), 
            'fecha_salida' : ('Fecha Salida'), 
            'turista' : ('Turista'), 
            'procedencia' : ('Procedencia'),             
        }        
        exclude = []
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'    

