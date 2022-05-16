from django import forms
from django.forms import ModelForm
from.models import *

#formulario

class productoForm(ModelForm):
    nombre = forms.CharField(min_length=10,max_length=20)
    precio = forms.IntegerField(min_value=400)
	
    class Meta:
        model = Producto
        fields = ['codigo','stock','nombre','marca','precio','descripcion','tipo','imagen']

        #]widgets = {
          #      'fecha_ingreso' : forms.SelectDateWidget(years=range(2020,2023))
        #}
class usuarioForm(ModelForm):
    nombre = forms.CharField(min_length=10, max_length=30)
    numero= forms.IntegerField(min_value=400)

    class Meta:
      model = Usuario
      fields =['rut','nombre','apellido','email','numero','tipo_usuario','imagen']