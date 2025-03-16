from django.db import models
from sistema_clinico.apps.reportes.models import Paciente

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    cc = models.CharField(max_length=20, unique=True)
    edad = models.IntegerField()
    genero = models.CharField(max_length=10)

class Examen(models.Model):
    tipo = models.CharField(max_length=100)
    ruta_imagen = models.CharField(max_length=255)
    ruta_resultado = models.CharField(max_length=255)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tipo} - {self.paciente.nombre}"
