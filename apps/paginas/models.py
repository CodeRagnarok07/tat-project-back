from django.db import models

# Create your models here.


def upload_path(instance, filename):
    if " " in instance.pagina.titulo_pagina:
        instance.pagina.titulo_pagina.replace(" ", "_")
    return '/'.join(['paginas',instance.pagina.titulo_pagina, filename])



class Pagina(models.Model):
    titulo_pagina = models.CharField(max_length=500)

    def __str__(self):
        return self.titulo_pagina


class Seccion(models.Model):
    titulo = models.CharField(max_length=500)
    icono = models.TextField(blank=True,null=True)
    imagen = models.ImageField(blank=True,null=True, upload_to=upload_path)
    text = models.TextField(blank=True,null=True)
    posicion = models.IntegerField()
    pagina = models.ForeignKey(Pagina, on_delete=models.CASCADE)
    def __str__(self):
        return f'#{self.posicion} {self.titulo}'

class Contenido(models.Model):
    titulo = models.CharField(max_length=500,blank=True,null=True)
    icono = models.TextField(blank=True,null=True)
    text = models.TextField(blank=True,null=True)
    posicion = models.IntegerField()
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE, related_name="contenido")
    def __str__(self):
        return f'#{self.posicion} {self.titulo}'


