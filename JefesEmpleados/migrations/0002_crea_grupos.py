# JefesEmpleados/migrations/0002_crea_grupos.py

from django.db import migrations

def crea_grupos(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Group.objects.get_or_create(name='Jefe')
    Group.objects.get_or_create(name='Empleado')

class Migration(migrations.Migration):

    dependencies = [
        ('JefesEmpleados', '0001_initial'),  # Asegúrate de que esta dependencia sea correcta
    ]

    operations = [
        migrations.RunPython(crea_grupos),
    ]