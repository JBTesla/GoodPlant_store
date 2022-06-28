import email
from pyexpat import model
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
    precio= models.IntegerField()
    descripcion=models.CharField(max_length=20)
    tipo= models.ForeignKey(TipoProducto, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="productos", null=True)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
       
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table ='db_producto'
class TipoUsuario(models.Model):
    tipo= models.CharField(max_length=20)
    def __str__(self):
        return self.tipo
    
    class Meta:
        db_table ='db_tipo_usuario'

class Usuario(models.Model):
    rut=models.IntegerField(null=False,primary_key=True)
    nombre=models.CharField(max_length=20)
    correo=models.CharField(max_length=20)
    numero=models.CharField(max_length=20)
    tipo=models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="usuarios", null=True)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.rut
    class Meta:
        db_table ='db_usuario'

class Despacho(models.Model):
    codigo = models.AutoField(null=False,primary_key=True)
    cantidad = models.IntegerField()
    fecha_compra = models.DateField(auto_now_add=True)
    producto = models.ForeignKey(Producto, on_delete= models.CASCADE)
    usuario = models.IntegerField()
    estado = models.CharField(max_length=50)

    def __str__(self):
        return self.codigo
        
    class Meta:
        db_table = 'db_despacho'    


class Items_Carrito(models.Model):
    id = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(null=True)
    user = models.IntegerField()

    def __str__(self):
        return self.id
        
    class Meta:
        db_table ='db_items_carrito'

class Suscripcion(models.Model):
    username=models.CharField(max_length=20,primary_key=True)
    is_suscrito=models.BooleanField(default=False)
    
    def __str__(self):
        return self.is_suscrito

    class Meta:
        db_table ='db_Suscripcion'