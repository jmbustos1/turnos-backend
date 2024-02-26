from django.shortcuts import render


from rest_framework import viewsets
from .models import Empleado, Marca
from .serializers import EmpleadoSerializer, MarcaSerializer

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer