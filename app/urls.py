from django.urls import path
from.views import *

urlpatterns = [
    path('', index,name="index"),
    path('perfil/',perfil,name="profile"),
    path('historial/', historial,name="history"),
    path('suscripcion/', suscripcion,name="suscribe"),
    path('seguimiento1/', seguimiento1,name="segui1"),
    path('seguimiento2/', seguimiento2,name="segui2"),
    path('seguimiento3/', seguimiento3,name="segui3"),
    path('productos/', productos,name="products"),
    path('agregar_productos/', agregar_productos,name="add_products"),
    path('modificar_productos/<codigo>/', modificar_productos,name="modify_products"),
    path('eliminar_productos/<codigo>/', eliminar_productos,name="eliminar_productos"),
    path('listar_productos/', listar_productos,name="list_products"),
    path('carrito/', carrito,name="cart"),
    path('pago_recibido/', pago_recibido,name="sucess"),
    path('eliminar_item/',eliminar_item,name="delete_item"),
    path('register/',register,name="register"),
]