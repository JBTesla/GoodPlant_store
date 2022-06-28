from django import forms
from django.forms import ModelForm
from.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

class FormularioUserResgistro(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

class suscripcionForm(ModelForm):

  class Meta:
      model = Suscripcion
      fields =['username','is_suscrito']