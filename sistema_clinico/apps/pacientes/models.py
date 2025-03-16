from django.db import models


class Paciente(models.Model):
    nombre = models.CharField(max_length=50)
    cc = models.CharField(max_length=10)
    fecha_nacimiento = models.IntegerField()
    genero = models.CharField(max_length=1)

    def __str__(self):
        return f"{self.cc} - {self.nombre}"
