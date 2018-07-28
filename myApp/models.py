from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Trabajo(models.Model):
    codigo = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=300, null=True)
    direccion = models.CharField(max_length=50)

    def __unicode__(self):
        return self.descripcion

    def __str__(self):
        return self.descripcion


class Contacter(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=60)
    subject = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.email

    def __str__(self):
        return self.email