# JefesEmpleados/serializers.py

from rest_framework import serializers
from .models import Empleado, Marca

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ['id', 'nombre', 'es_jefe']

class MarcaSerializer(serializers.ModelSerializer):
    empleado = serializers.SlugRelatedField(slug_field='nombre', queryset=Empleado.objects.all())
    
    class Meta:
        model = Marca
        fields = ['id', 'empleado', 'fecha', 'marcado']