from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Group
from .models import Empleado

@receiver(post_save, sender=User)
def crear_perfil_empleado(sender, instance, created, **kwargs):
    if created:
        # Verifica si el usuario es un jefe
        if not instance.groups.filter(name='Jefe').exists():
            Empleado.objects.create(usuario=instance)
