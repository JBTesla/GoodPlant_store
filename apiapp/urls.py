# CORRESPONDE A LAS URLS QUE SE UTILIZAAN
from django.urls import path , include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('producto', ProductoViewSet)
router.register('tipo_producto', TipoProductoViewSet)
router.register('usuario', UsuarioViewSet)
router.register('tipo_usuario', TipoUsuarioViewSet)
router.register('suscripcion', SuscripcionViewSet)
urlpatterns = [
    path('api/',include(router.urls)),
]
