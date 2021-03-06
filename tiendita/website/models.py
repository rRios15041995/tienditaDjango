from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from datetime import datetime

# Create your models here.

class Producto(models.Model):
	id = models.CharField(max_length=75, null=False, primary_key=True)
	nombre = models.CharField(max_length=100, null=False)
	tipo =  models.CharField(max_length=20, null=False)
	descripcion = models.CharField(max_length=300, null=False)
	precio = models.DecimalField(decimal_places=2, max_digits=5, null=False)
	foto = models.FileField(null=True)

	def __str__(self):
		return '%s %s %s %i' % (self.nombre, self.tipo, self.descripcion, self.precio)

	def get_absolute_url(self):
		return reverse('menu:new_item')

class Cliente(models.Model):
	id = models.CharField(max_length=50, null=False, primary_key=True)
	nombre = models.CharField(max_length=50, null=False)
	apellido1 = models.CharField(max_length=50, null=False)
	apellido2 = models.CharField(max_length=50, null=False)
	dob = models.DateField(null=False)
	saldo = models.DecimalField(decimal_places=2, max_digits=8, default=0.0, null=False)
	deuda = models.DecimalField(decimal_places=2, max_digits=5, default=0.0, null=False)
	foto = models.FileField(null=True)

	def __str__(self):
		return '%s %s %s %s %i' % (self.nombre, self.apellido1, self.apellido2, self.dob)


class Pedido(models.Model):
	id = models.CharField(max_length=8, null=False, primary_key=True)
	cliente = models.ForeignKey(Cliente, null=False, on_delete=models.CASCADE)
	fecha = models.DateTimeField(auto_now_add=True, null=False)

	def __str__(self):
		return '%s %s' % (self.cliente, self.fecha)

class ProductosPedido(models.Model):
	pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
	producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
	cantidad =  models.IntegerField()

	def __str__(self):
		return '%s %s ' % (self.pedido, self.producto, self.cantidad)
