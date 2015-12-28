from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Persona(models.Model):
    tipo_persona = models.CharField(max_length=1)
    tipo_identificacion = models.CharField(max_length=2)
    identificacion = models.CharField(max_length=64)
    nombres = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255,null=True,blank=True)
    fecha_nacimiento = models.DateField(null=True,blank=True)
    celular = models.CharField(max_length=20,null=True,blank=True)
    email_personal = models.CharField(max_length=20,null=True,blank=True)
