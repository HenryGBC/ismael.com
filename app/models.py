from django.db import models

# Create your models here.
class Tipo(models.Model):
	nombre = models.CharField(max_length= 100)
	slug_tipo = models.SlugField(max_length=100, blank=True)

	def save(self, *args, **kwargs):
		self.slug_tipo = self.nombre.lower().replace(' ','-')
		super(Tipo, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.nombre


class Ingrediente(models.Model):
	nombre = models.CharField(max_length= 100)
	cantidad = models.IntegerField(default = 0)
	unidad = models.CharField(max_length= 20)

	def __unicode__(self):
		return  "%s -  %s - %s" % (self.nombre, self.cantidad, self.unidad)


	
class Plato(models.Model):
	tipo = models.ForeignKey(Tipo)
	nombre = models.CharField(max_length= 100)
	descripcionCorta = models.CharField(max_length= 500)
	descripcion = models.CharField(max_length= 1000)
	img = models.ImageField(upload_to='media/')
	slug = models.SlugField(max_length=100, blank=True)
	ingredientes =models.ManyToManyField(Ingrediente, blank=True)


	def save(self, *args, **kwargs):
		self.slug = self.nombre.lower().replace(' ','-')
		super(Plato, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.nombre


class Menu(models.Model):
	plato = models.ForeignKey(Plato)
	precio = models.IntegerField(default = 0)
	fecha = models.DateField()

	def __unicode__(self):
		return "%s -  %s - %s" % (self.plato, self.precio, self.fecha)


class Email(models.Model):
	email = models.EmailField(max_length= 100)

	def __unicode__(self):
		return self.email