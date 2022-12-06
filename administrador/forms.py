from django.forms import *
from .models import *

class HotelForm(ModelForm):
    class Meta:
        model = Hotel
        fields = ['nombre_hotel', 'municipio','direccion', 'telefono', 'estado',  'celular', 'eslogan', 'logo', 'estrellas']
        labels = {
            'nombre_hotel':('Nombre hotel'), 
            'municipio':('Municipio'), 
            'direccion':('Direccion'), 
            'telefono':('Telefono'), 
            'estado':('Estado'),  
            'celular':('Celular'), 
            'eslogan':('Eslogan'), 
            'logo':('Logo'), 
            'estrellas':('Estrellas')
        }
        #widgets = {'mes': TextInput(attrs={'readonly': 'readonly'}), 'gestion': TextInput(attrs={'readonly': 'readonly'})}
        widgets = {'estrellas': HiddenInput(attrs={'type': 'hidden'})}
        exclude = ['usuario']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'   

class UsuarioForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'is_active']
        labels = {
            'username':('Usuario'), 
            'first_name':('Nombre'), 
            'last_name':('Apellidos'), 
            'is_active':('Estado')
        }
        #widgets = {'mes': TextInput(attrs={'readonly': 'readonly'}), 'gestion': TextInput(attrs={'readonly': 'readonly'})}
        exclude = []
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'  

class UsuarioForm3(ModelForm):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_active']
        labels = {
            'id':('Id'), 
            'username':('Usuario'), 
            'first_name':('Nombre'), 
            'last_name':('Apellidos'), 
            'email':('Email'), 
            'is_active':('Estado')
        }
        #widgets = {'mes': TextInput(attrs={'readonly': 'readonly'}), 'gestion': TextInput(attrs={'readonly': 'readonly'})}
        exclude = []
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'  