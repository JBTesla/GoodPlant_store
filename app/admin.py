from django.contrib import admin
from.models import *

# Register your models here.
class productosAdmin(admin.ModelAdmin):
     list_display=['codigo','stock','nombre','marca','precio','descripcion','tipo','imagen','create_at','update_at']
     search_fields=['codigo']
     list_per_page= 5


class despachoAdmin(admin.ModelAdmin):
     list_display=['codigo','cantidad','fecha_compra','producto','usuario','estado']
     search_fields=['codigo']
     list_per_page= 5

class usuarioAdmin(admin.ModelAdmin):
     list_display=['rut','nombre','correo','numero','tipo','imagen','create_at','update_at']
     search_fields = ['rut']
     list_per_page = 5

class suscripcioAdmin(admin.ModelAdmin):
     list_display= ['username','is_suscrito']
     search_fields= ['username']
     list_per_page= 5

class carritoAdmin(admin.ModelAdmin):
     list_display =['id','producto','cantidad','user']
     search_fields=['user']
     list_per_page=5

admin.site.register(TipoProducto)
admin.site.register(Producto, productosAdmin)
admin.site.register(TipoUsuario)
admin.site.register(Usuario,usuarioAdmin)
admin.site.register(Items_Carrito,carritoAdmin)
admin.site.register(Suscripcion,suscripcioAdmin)
admin.site.register(Despacho,despachoAdmin)