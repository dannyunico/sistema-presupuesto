from django.db import models

# Create your models here.

class Material(models.Model):

	codigo = models.CharField(max_length = 500)
	title = models.CharField(max_length = 500)
	unidad = models.CharField(max_length = 500)
	precio = models.DecimalField(max_digits=15,decimal_places=2)
	cantidad = models.IntegerField(default=2)  

class Herramientas(models.Model):

	codigo = models.CharField(max_length = 500)
	titulo = models.CharField(max_length = 500)
	COP = models.DecimalField(max_digits=15,decimal_places=2) 
	precio = models.DecimalField(max_digits=15,decimal_places=2)

class LaborIndirecta(models.Model):

	codigo = models.CharField(max_length = 500)
	nombre = models.CharField(max_length = 500)
	jornal =  models.DecimalField(max_digits=15,decimal_places=2)


class Factura(models.Model):

	Titulo = models.CharField(max_length = 500)
	Numero_Factura = models.CharField(max_length = 500)
	Cod_Factura = models.CharField(max_length = 500)
	Material = models.ManyToManyField(Material)
	Herramientas = models.ManyToManyField(Herramientas)
	LaborIndirecta = models.ManyToManyField(LaborIndirecta)

class Presupuesto(models.Model):

	Factura = models.ForeignKey(Factura, null = True, blank = True, on_delete = models.CASCADE)







