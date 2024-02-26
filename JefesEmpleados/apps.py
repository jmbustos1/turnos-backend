from django.apps import AppConfig

class JefesempleadosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'JefesEmpleados'

    def ready(self):
        # Importa las señales aquí para evitar el error AppRegistryNotReady
        from . import signals