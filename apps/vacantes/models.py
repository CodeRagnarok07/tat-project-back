from email.policy import default
from django.db import models

# Create your models here.


class Vacante(models.Model):
    titulo = models.CharField(max_length=500)
    lugar = models.CharField(max_length=500)
    requisitos = models.TextField()
    email = models.EmailField()
    expiracion = models.DateField()
    order = models.IntegerField(default=1)

    def __str__(self):
        return self.titulo