from django.urls import path
from.views import *

urlpatterns = [
    path('', index,name="index"),
    path('perfil/',perfil,name="profile"),
    path('perfil_admin/',perfil_admin,name="profile_admin"),
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
    path('agregar_usuarios/',agregar_usuarios,name="add_users"),
    path('modificar_usuarios/<rut>',modificar_usuarios,name="modify_users"),
    path('eliminar_usuario/<rut>/',eliminar_usuario,name="eliminar_usuario"),
    path('listar_usuarios/',listar_usuarios,name="list_users"),
    path('carrito/', carrito,name="cart"),
    path('pago_recibido/', pago_recibido,name="sucess"),
    path('eliminar_item/',eliminar_item,name="delete_item"),
]