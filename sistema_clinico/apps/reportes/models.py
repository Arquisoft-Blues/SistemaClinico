from django.db import models

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    cc = models.CharField(max_length=20, unique=True)
    edad = models.IntegerField()
    genero = models.CharField(max_length=10)
