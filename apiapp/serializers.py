# SE ENCARGA DE HACER EL CRUD DESDE JSON

from app.models import *
from rest_framework import serializers

class TipoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProducto
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'