from django.db import models

# Create your models here.
class Cine(models.Model):
    Nombre = models.CharField(max_length=60)
    Cuidad = models.CharField(max_length=60)
class Venta(models.Model):
    Fecha= models.CharField(max_length=60)
    Total = models.CharField(max_length=60)
class Empleado(models.Model):
    Nombre = models.CharField(max_length=60)
    Puesto= models.CharField(max_length=60)
class Boleto(models.Model):
    Precio = models.CharField(max_length=60)
    Asiento = models.CharField(max_length=60)
class Cliente(models.Model):
    id_Client3 = models.CharField(max_length=60)
    Correo= models.CharField(max_length=60)
class Proyeccion(models.Model):
     id_Proyeccion = models.CharField(max_length=60)
     Hora= models.CharField(max_length=60)
class Pelicula(models.Model):
    id_Pelicula = models.CharField(max_length=60)
    Titulo = models.CharField(max_length=60)
class Sala(models.Model):
    id_Sala = models.CharField(max_length=60)
    Precio = models.CharField(max_length=60)