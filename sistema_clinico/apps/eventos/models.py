from django.db import models
from sistema_clinico.apps.pacientes.models import Paciente


class Evento(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name="eventos")
    descripcion = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
