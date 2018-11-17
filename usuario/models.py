from django.db import models
from django.db.models import Model
# Create your models here.
class Usuario(Model):
	id_usuario=models.IntegerField(primary_key=True)
	nombre =models.CharField(max_length=50)
	sexo =models.CharField(max_length=10)
	Edad =models.IntegerField()
	telefono =models.CharField(max_length=10)
	email =models.EmailField()
	domicilio=models.TextField(max_length=50)



class Proyecto(Model):
	id_proyecto=models.IntegerField(primary_key=True)
	nombre_proyecto =models.CharField(max_length=50)
	Localizacion =models.CharField(max_length=50)
	Monto =models.IntegerField()
	Plazo_Ejecucion =models.DateField(max_length=10)
	Detalle_monto =models.TextField()
	