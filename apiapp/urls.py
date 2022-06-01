# CORRESPONDE A LAS URLS QUE SE UTILIZAAN
from django.urls import path , include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('producto', ProductoViewSet)

urlpatterns = [
    path('api/',include(router.urls)),
]