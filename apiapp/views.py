from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from app.models import *

# Create your views here.

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class TipoProductoViewSet(viewsets.ModelViewSet):
    queryset = TipoProducto.objects.all()
    serializer_class = TipoProductoSerializer

class TipoUsuarioViewSet(viewsets.ModelViewSet):
    queryset=TipoUsuario.objects.all()
    serializer_class= TipoUsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset=Usuario.objects.all()
    serializer_class= UsuarioSerializer

class SuscripcionViewSet(viewsets.ModelViewSet):
    queryset=Suscripcion.objects.all()
    serializer_class= UsuarioSerializer