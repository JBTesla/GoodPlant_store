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

class despachoAdmin(admin.ModelAdmin):
     list_display=['codigo','nombre','marca','cantidad','fechaCompra','fechaEstimadaEntrega','precio','estadoDespacho']
     search_fields=['codigo']
     list_per_page= 5



admin.site.register(TipoProducto)
admin.site.register(Producto, productosAdmin)
admin.site.register(historialCompra,historialAdmin)
admin.site.register(Suscripcion)
admin.site.register(estadoDespacho)
admin.site.register(despacho,despachoAdmin)