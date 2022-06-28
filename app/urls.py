from django.urls import path
from.views import *

urlpatterns = [
    path('', index,name="index"),
    path('perfil/',perfil,name="profile"),
    path('historial/<id>', historial,name="history"),
    path('suscripcion/', suscripcion,name="suscribe"),
    path('eliminar_suscripcion/<username>/', eliminar_suscripcion,name="eliminar_suscripcion"),
    path('seguimiento_despacho/', seguimiento_despacho,name="seguimiento_despacho"),
    path('despacho_admin/', despacho_admin,name="despacho_admin"),
    path('eliminar_despacho/<codigo>/', eliminar_despacho,name="eliminar_despacho"),
    path('productos/', productos,name="products"),
    path('productos_api/', productosApi,name="productosApi"),
    path('agregar_productos/', agregar_productos,name="add_products"),
    path('modificar_productos/<codigo>/', modificar_productos,name="modify_products"),
    path('eliminar_productos/<codigo>/', eliminar_productos,name="eliminar_productos"),
    path('listar_productos/', listar_productos,name="list_products"),
    path('carrito/<id>/', carrito,name="cart"),
    path('pago_recibido/', pago_recibido,name="sucess"),
    path('eliminar_item/<codigo>/',eliminar_item,name="delete_item"),
    path('limpiar_carrito/',limpiar_carrito,name="limpiar_carrito"),
    path('register/',register,name="register"),
    path('apiCustom/', apiCustom,name="apiCustom"),
]