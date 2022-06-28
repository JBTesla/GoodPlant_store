# SE ENCARGA DE HACER EL CRUD DESDE JSON

from dataclasses import fields
from app.models import *
from rest_framework import serializers

class TipoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProducto
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    #nombre_tipo = serializers.CharField(read_only=True,source='tipo.tipo')
    tipo = TipoProductoSerializer(read_only=True)

    class Meta:
        model = Producto
        fields = '__all__'
class TipoUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model= TipoUsuario
        fields ='__all__'
class UsuarioSerializer(serializers.ModelSerializer):
    tipo = TipoProductoSerializer(read_only=True)
    class Meta:
        model= Usuario
        fields='__all__'
class Suscripcion(serializers.ModelSerializer):
    class Meta:
        model=Suscripcion
        fields='__all__'