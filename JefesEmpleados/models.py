from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Empleado(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    es_jefe = models.BooleanField(default=False)

class Marca(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha = models.DateField()
    marcado = models.BooleanField(default=False)
