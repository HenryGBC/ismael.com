from django.db import models

# Create your models here.
class Tipo(models.Model):
	nombre = models.CharField(max_length= 100)

	def __unicode__(self):
		return self.nombre


	
class Plato(models.Model):
	tipo = models.ForeignKey(Tipo)
	nombre = models.CharField(max_length= 100)
	descripcion = models.CharField(max_length= 500)
	ruta = models.CharField(max_length= 100)

	def __unicode__(self):
		return self.nombre

class Ingrediente(models.Model):
	plato = models.ForeignKey(Plato)
	nombre = models.CharField(max_length= 100)
	cantidad = models.IntegerField(default = 0)
	unidad = models.CharField(max_length= 20)

	def __unicode__(self):
		return self.nombre

class Menu(models.Model):
	plato = models.ForeignKey(Plato)
	precio = models.IntegerField(default = 0)
	fecha = models.DateField()

	def __unicode__(self):
		return "%s -  %s - %s" % (self.plato, self.precio, self.fecha)

