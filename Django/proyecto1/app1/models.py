from django.db import models
import datetime

# Create your models here.

class Categoria (models.Model):
	nombre = models.CharField(max_length= 30)
	descripcion = models.CharField(max_length= 100)
	def __str__(self):
		return self.nombre

class Producto (models.Model):
	nombre= models.CharField(max_length=30)
	precio= models.FloatField()
	stock= models.IntegerField()
	def __str__(self):
		return self.nombre

class Venta (models.Model):
	descuento=models.FloatField()
	fecha=models.DateField()
	def __str__(self):
		return str(self.id)

class Direccion_proveedor(models.Model):
	calle=models.CharField(max_length=30)
	numero=models.CharField(max_length=5)
	comuna=models.CharField(max_length=100)
	ciudad=models.CharField(max_length=50)
	def __str__(self):
		return str(f"{self.calle} {self.numero}")

class Proveedor (models.Model):
	rut = models.CharField(max_length=100, primary_key=True)
	nombre=models.CharField(max_length=30)
	web=models.URLField()
	direccion = models.ForeignKey(Direccion_proveedor,on_delete=models.CASCADE)
	telefono=models.IntegerField(max_length=10)
	def __str__(self):
		return self.nombre

class Telefonos_clientes (models.Model):
	telefono=models.CharField(max_length=10)
	def __str__(self):
		return self.telefono

class Direccion_cliente(models.Model):
	calle=models.CharField(max_length=30)
	numero=models.CharField(max_length=5)
	comuna=models.CharField(max_length=100)
	ciudad=models.CharField(max_length=50)
	def __str__(self):
		return str(f"{self.calle} {self.numero}")

class Producto_venta(models.Model):
	cantidad=models.IntegerField()
	Producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
	Venta = models.ForeignKey(Venta,on_delete=models.CASCADE)
	def __str__(self):
		return str(self.id)

class Cliente(models.Model):
	rut = models.CharField(max_length=100, primary_key=True)
	nombre=models.CharField(max_length=30)
	direccion = models.ForeignKey(Direccion_cliente,on_delete=models.CASCADE)
	telefono= models.ForeignKey(Telefonos_clientes,on_delete=models.CASCADE)
	def __str__(self):
		return self.nombre