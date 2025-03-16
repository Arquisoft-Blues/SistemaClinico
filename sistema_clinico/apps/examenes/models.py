from django.db import models
from sistema_clinico.apps.pacientes.models import Paciente
from sistema_clinico.apps.medicos.models import Medico


class Examen(models.Model):
    tipo = models.CharField(max_length=100)
    fecha = models.DateField()
    ruta_imagen = models.CharField(max_length=255)
    ruta_resultado = models.CharField(max_length=255)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name="examenes")
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name="examenes")

    def __str__(self):
        return f"{self.tipo} - {self.paciente.nombre} - {self.fecha}"
