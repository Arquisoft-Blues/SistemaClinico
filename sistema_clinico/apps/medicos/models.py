from django.db import models


class Medico(models.Model):
    nombre = models.CharField(max_length=50)
    cc = models.CharField(max_length=10)
    especialidad = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.cc} - {self.nombre} - {self.especialidad}"
