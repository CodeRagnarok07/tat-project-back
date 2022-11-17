from email.policy import default
from django.db import models

# Create your models here.

from core.utils import auto_slug


def upload_path(instance, filename):
    if " " in instance.nombre:
        instance.nombre.replace(" ", "_")
    return '/'.join(['equipo_y_autoridades',instance.nombre, filename])

class Oficina(models.Model):
    lugar = models.CharField(max_length=500)
    order = models.IntegerField(default=1)
    calle = models.CharField(max_length=500, blank=True, null=True)
    tlf = models.CharField(max_length=500, blank=True, null=True)
    correo = models.EmailField(max_length=500, blank=True, null=True)
    mapa = models.URLField()
    def __str__(self):
        return self.lugar

class Departamento(models.Model):
    titulo = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    def __str__(self):
        return self.titulo



class Autoridad(models.Model):
    nombre = models.CharField(max_length=500)
    titulo = models.CharField(max_length=500)
    imagen = models.ImageField(upload_to="nosotros/autoridades")
    text = models.TextField()

    slug = models.SlugField(unique=True, default="",null=True,blank=True)
    def save(self, *args, **kwargs):
        self.slug = auto_slug(self.titulo, Autoridad)
        print(self.slug)
        super(Autoridad, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.titulo} {self.nombre}'

class Equipo(models.Model):
    nombre = models.CharField(max_length=500)
    titulo = models.CharField(max_length=500)
    imagen = models.ImageField(upload_to=upload_path)
    text = models.TextField()

    slug = models.SlugField(unique=True, default="",null=True,blank=True)

    def save(self, *args, **kwargs):
        self.slug = auto_slug(self.titulo, Equipo)
        print(self.slug)
        super(Equipo, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.titulo} {self.nombre}'


