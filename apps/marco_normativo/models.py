from email.policy import default
from django.db import models

# Create your models here.
import datetime
from django.utils.translation import gettext_lazy as _

class Competencia(models.Model):
    titulo = models.CharField(max_length=500)
    order = models.IntegerField(default=1)
    text = models.TextField()
    def __str__(self):
        return self.titulo


# solo año parametro de busqueda

YEAR_CHOICES = []
for r in range(2005, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r,r))


class LeyesYDecreto(models.Model):
    titulo = models.CharField(max_length=500)
    año = models.IntegerField(_('año'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    archivo = models.FileField(upload_to="marco-normativo/leyes-y-decretos")
    
    @property
    def ver(self):
        return self.archivo.url
    @property
    def descargar(self):
        return self.pk
    def __str__(self):
        return self.titulo

class Acuerdo(models.Model):
    titulo = models.CharField(max_length=500)
    año = models.IntegerField(_('año'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    archivo = models.FileField(upload_to="marco-normativo/acuerdos")
    
    @property
    def ver(self):
        return self.archivo.url
    @property
    def descargar(self):
        return self.pk
    def __str__(self):
        return self.titulo

class Convenio(models.Model):
    titulo = models.CharField(max_length=500)
    año = models.IntegerField(_('año'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    archivo = models.FileField(upload_to="marco-normativo/convenios")
    
    @property
    def ver(self):
        return self.archivo.url
    @property
    def descargar(self):
        return self.pk
    def __str__(self):
        return self.titulo

class Edicto(models.Model):
    titulo = models.CharField(max_length=500)
    año = models.IntegerField(_('año'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    archivo = models.FileField(upload_to="marco-normativo/edictos")
    
    @property
    def ver(self):
        return self.archivo.url
    @property
    def descargar(self):
        return self.pk
    def __str__(self):
        return self.titulo

class Flujograma(models.Model):
    titulo = models.CharField(max_length=500)
    inicio = models.DateField(auto_now=True)
    final = models.DateField(auto_now=True)
    archivo = models.FileField(upload_to="marco-normativo/flujograma")
    
    @property
    def ver(self):
        return self.archivo.url
    @property
    def descargar(self):
        return self.pk
    def __str__(self):
        return self.titulo

