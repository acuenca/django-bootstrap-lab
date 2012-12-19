from django.db import models


class Contacto(models.Model):
	nombres = models.CharField(max_length=100)
	apellidos = models.CharField(max_length=200)
	fn = models.DateTimeField('Fecha de nacimiento')
	email = models.CharField(max_length=100)
	twitter = models.CharField(max_length=100)