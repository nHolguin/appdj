from django.db import models
from django.utils import timezone

# Create your models here.
class Empleado(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    posicion = models.CharField(max_length=200)
    oficina = models.CharField(max_length=200)
    edad = models.IntegerField()
    inicio = models.DateTimeField(default=timezone.now)
    salario = models.FloatField()

class Reporte(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
