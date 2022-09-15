from pyexpat import model
from django.db import models

# Create your models here.

class Categoria (models.Model):
	nombre = models.CharField(max_length= 30)
	descripcion = models.CharField(max_length= 100)

class Producto (models.Model):
	nombre= models.CharField(max_length=30)
	precio= models.FloatField()
	stock= models.IntegerField()

class Venta (models.Model):
	descuento=models.FloatField()
	fecha=models.DateField()

class Direccion_proveedor(models.Model):
	calle=models.CharField(max_length=30)
	numero=models.CharField(max_length=5)
	comuna=models.CharField(max_length=100)
	ciudad=models.CharField(max_length=50)

class Proveedor (models.Model):
	rut = models.CharField(max_length=100, primary_key=True)
	nombre=models.CharField(max_length=30)
	web=models.URLField()
	direccion = models.ForeignKey(Direccion_proveedor,on_delete=models.CASCADE)
	telefono=models.IntegerField(max_length=10)

class Telefonos_clientes (models.Model):
	telefono=models.CharField(max_length=10)

class Direccion_cliente(models.Model):
	calle=models.CharField(max_length=30)
	numero=models.CharField(max_length=5)
	comuna=models.CharField(max_length=100)
	ciudad=models.CharField(max_length=50)

class Producto_venta(models.Model):
	cantidad=models.IntegerField()

class Cliente(models.Model):
	rut = models.CharField(max_length=100, primary_key=True)
	nombre=models.CharField(max_length=30)
	direccion = models.ForeignKey(Direccion_cliente,on_delete=models.CASCADE)
	telefono= models.ForeignKey(Telefonos_clientes,on_delete=models.CASCADE)
