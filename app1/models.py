#from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Materia(models.Model):
    """ Categorias para clasificar las fotos """
    
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre


class Estudiante(models.Model):
    """ Fotos del album """

    materia = models.ForeignKey(Materia, null=True, blank=True)
    nombres = models.CharField(max_length=50, default='No nombres')
 
    
    def __unicode__(self):
        return self.nombres