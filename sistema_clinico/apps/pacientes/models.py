from django.db import models
from datetime import date


class GeneroEnum(models.TextChoices):
    MASCULINO = "M"
    FEMENINO = "F"


class Paciente(models.Model):
    nombre = models.CharField(max_length=50)
    cc = models.CharField(max_length=10)
    edad = models.IntegerField(null=False)
    genero = models.CharField(max_length=1, choices=GeneroEnum.choices)

    def __str__(self):
        return f"{self.cc} - {self.nombre}"
