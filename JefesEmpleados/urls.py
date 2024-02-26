# JefesEmpleados/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'empleados', views.EmpleadoViewSet)
router.register(r'marcas', views.MarcaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
