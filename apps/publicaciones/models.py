from email.policy import default
from django.db import models

# Create your models here.
import datetime
from django.utils.translation import gettext_lazy as _


class CategoriasResoluciones(models.Model):
    titulo = models.CharField(max_length=500)
    def __str__(self):
        return self.titulo

YEAR_CHOICES = []
for r in range(2005, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r,r))

class Resolucion(models.Model):
    titulo = models.CharField(max_length=500)
    año = models.IntegerField(_('año'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)

    archivo = models.FileField(upload_to='uploads/publicaciones/resoluciones/%Y/%m/%d/')
    tag = models.ForeignKey(CategoriasResoluciones, on_delete=models.CASCADE, related_name="resolucion")

    @property
    def categoria(self):
        return self.tag.titulo
    @property
    def ver(self):
        return self.archivo.url
    @property
    def descargar(self):
        return self.pk
    def __str__(self):
        return self.titulo

class Ponencia(models.Model):
    titulo = models.CharField(max_length=500)
    def __str__(self):
        return self.titulo

class PonenciasArchivos(models.Model):
    titulo = models.CharField(max_length=500)
    archivo = models.FileField(upload_to='uploads/publicaciones/ponencias/%Y/%m/%d/')
    categoria = models.ForeignKey(Ponencia, on_delete=models.CASCADE, related_name="archivos")

    @property
    def ver(self):
        return self.archivo.url
    @property
    def descargar(self):
        return self.pk
        
    def __str__(self):
        return self.titulo

class RevistasTributaria(models.Model):
    titulo = models.CharField(max_length=500)
    archivo = models.FileField(upload_to='uploads/publicaciones/revistas-tributaria/%Y/%m/%d/')

    @property
    def ver(self):
        return self.archivo.url
    @property
    def descargar(self):
        return self.pk
    def __str__(self):
        return self.titulo


class Memorias(models.Model):
    titulo = models.CharField(max_length=500)
    archivo = models.FileField(upload_to='uploads/publicaciones/memorias/%Y/%m/%d/')

    @property
    def ver(self):
        return self.archivo.url
    @property
    def descargar(self):
        return self.pk
    def __str__(self):
        return self.titulo


class Otros(models.Model):
    titulo = models.CharField(max_length=500)
    archivo = models.FileField(upload_to='uploads/publicaciones/otros/%Y/%m/%d/')

    @property
    def ver(self):
        return self.archivo.url
    @property
    def descargar(self):
        return self.pk
    def __str__(self):
        return self.titulo