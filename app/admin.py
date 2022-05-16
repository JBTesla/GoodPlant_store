from django.contrib import admin
from.models import *

# Register your models here.
class productosAdmin(admin.ModelAdmin):
     list_display=['codigo','stock','nombre','marca','precio','descripcion','tipo','imagen','create_at','update_at']
     search_fields=['codigo']
     list_per_page= 5

class historialAdmin(admin.ModelAdmin):
     list_display=['codigo','nombre','marca','cantidad','fechaCompra','precio','tipo']
     search_fields=['codigo']
     list_per_page= 5

class historialSubAdmin(admin.ModelAdmin):
     list_display=['tipoSuscripcion','fechaInicio','fechaTermino','estado','monto']
     search_fields=['tipoSuscripcion']
     list_per_page= 5

class despachoAdmin(admin.ModelAdmin):
     list_display=['codigo','nombre','marca','cantidad','fechaCompra','fechaEstimadaEntrega','precio','estadoDespacho']
     search_fields=['codigo']
     list_per_page= 5

class usuarioAdmin(admin.ModelAdmin):
     list_display=['rut','nombre','apellido','email','numero','tipo_usuario']
     search_fields=['rut']
     list_per_page: 5
admin.site.register(tipoUsuario)
admin.site.register(TipoProducto)
admin.site.register(Producto, productosAdmin)
admin.site.register(historialCompra,historialAdmin)
admin.site.register(estadoSuscripcion)
admin.site.register(historialSuscripcion,historialSubAdmin)
admin.site.register(estadoDespacho)
admin.site.register(despacho,despachoAdmin)
admin.site.register(Usuario,usuarioAdmin)