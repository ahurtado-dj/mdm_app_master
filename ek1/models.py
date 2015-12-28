from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Tercero(models.Model):
    ter_tipo = models.CharField(max_length=1)
    ter_tipodoc = models.CharField(max_length=2)
    ter_ident = models.CharField(max_length=64)
    ter_nom = models.CharField(max_length=255)
    ter_ap1= models.CharField(max_length=255,null=True,blank=True)
    ter_ap2= models.CharField(max_length=255,null=True,blank=True)
    ter_telefono = models.CharField(max_length=20,null=True,blank=True)
    ter_email = models.CharField(max_length=20,null=True,blank=True)
    x_sync_corr1 = models.CharField(max_length=255,null=True,blank=True)