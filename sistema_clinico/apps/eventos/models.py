from django.db import models
from sistema_clinico.apps.reportes.models import Paciente

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    cc = models.CharField(max_length=20, unique=True)
    edad = models.IntegerField()
    genero = models.CharField(max_length=10)

class EventoClinico(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name="eventos")
    descripcion = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
