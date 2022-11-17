from django.contrib import admin

# Register your models here.
from django_summernote.admin import SummernoteModelAdmin

from .models import Noticia, GaleriaNoticia, HaciendoDiferencia, GaleriaHaciendoDiferencia, Congreso, GaleriaCongreso

# NOTICIAS
class GaleriaNoticiaInline(admin.StackedInline):
    extra = 1
    model = GaleriaNoticia

@admin.register(Noticia)
class SeccionAdmin(SummernoteModelAdmin):
    list_display = ( 'fecha','titulo',  )
    list_filter = ('fecha',)
    exclude = ('slug',)

    inlines = [GaleriaNoticiaInline, ]

# HaciendoDiferencia
class GaleriaHaciendoDiferenciaInline(admin.StackedInline):
    extra = 1
    model = GaleriaHaciendoDiferencia

@admin.register(HaciendoDiferencia)
class SeccionAdmin(SummernoteModelAdmin):
    list_display = ( 'fecha','titulo',  )
    list_filter = ('fecha',)
    inlines = [GaleriaHaciendoDiferenciaInline, ]

# Congreso
class GaleriaCongresoInline(admin.StackedInline):
    extra = 1
    model = GaleriaCongreso

@admin.register(Congreso)
class SeccionAdmin(SummernoteModelAdmin):
    list_display = ( 'fecha','titulo',  )
    list_filter = ('fecha',)
    inlines = [GaleriaCongresoInline, ]