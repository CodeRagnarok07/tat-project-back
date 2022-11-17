from email.policy import default
from django.db import models

# Create your models here.


class PreguntasFrecuente(models.Model):
    titulo = models.CharField(max_length=500)
    order = models.IntegerField(default=1)
    text = models.TextField()
    def __str__(self):
        return self.titulo