import email
from django import db
from django.db import models

# Create your models here.
class TipoProducto(models.Model):
    tipo = models.CharField(max_length=20)

    def __str__(self):
        return self.tipo
    class Meta:
        db_table ='db_tipo_producto'    

class Producto(models.Model):
    codigo= models.IntegerField(null=False,primary_key=True)
    stock=models.IntegerField()
    nombre =models.CharField(max_length=20)
    marca= models.CharField(max_length=20)
    precio= models.CharField(max_length=20)
    descripcion=models.CharField(max_length=20)
    tipo= models.ForeignKey(TipoProducto, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="productos", null=True)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    
    class Meta:
        db_table ='db_producto'

class historialCompra(models.Model):
    codigo=models.ForeignKey(Producto, on_delete=models.CASCADE)
    nombre=models.CharField(max_length=20)
    marca=models.CharField(max_length=20)
    cantidad=models.IntegerField()
    fechaCompra=models.DateField()
    precio=models.CharField(max_length=20)
    tipo= models.ForeignKey(TipoProducto, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    class Meta:
        db_table ='db_historial'

class estadoSuscripcion(models.Model):
    estadoSuscripcion = models.CharField(max_length=20)

    def __str__(self):
        return self.estadoSuscripcion
    class Meta:
        db_table ='db_estadoSus'

class historialSuscripcion(models.Model):
    tipoSuscripcion=models.CharField(max_length=20)
    fechaInicio=models.DateField()
    fechaTermino=models.DateField()
    estado=models.ForeignKey(estadoSuscripcion, on_delete=models.CASCADE)
    monto=models.CharField(max_length=20)
    
    def __str__(self):
        return self.tipoSuscripcion
    class Meta:
        db_table ='db_suscripcion'

class estadoDespacho(models.Model):
    estadoDespacho = models.CharField(max_length=20)

    def __str__(self):
        return self.estadoDespacho
    class Meta:
        db_table ='db_estadoDesp'

class despacho(models.Model):
    codigo=models.IntegerField()
    nombre=models.CharField(max_length=20)
    marca=models.CharField(max_length=20)
    cantidad=models.IntegerField()
    fechaCompra=models.DateField()
    fechaEstimadaEntrega=models.DateField()
    precio=models.CharField(max_length=20)
    estadoDespacho = models.ForeignKey(estadoDespacho, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    class Meta:
        db_table ='db_despacho'

class Items_Carrito(models.Model):
    codigo=models.ForeignKey(Producto, on_delete=models.CASCADE)

    class Meta:
        db_table ='db_items_carrito'