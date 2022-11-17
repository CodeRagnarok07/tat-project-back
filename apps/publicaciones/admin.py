from django.contrib import admin

# Register your models here.
from django_summernote.admin import SummernoteModelAdmin

from .models import Resolucion, CategoriasResoluciones, Ponencia, PonenciasArchivos, RevistasTributaria,Memorias

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('text',)


admin.site.register(Resolucion)
admin.site.register(Memorias)
admin.site.register(CategoriasResoluciones)
admin.site.register(PonenciasArchivos)
admin.site.register(RevistasTributaria)


class PonenciasArchivosInline(admin.StackedInline):
    extra = 1
    model = PonenciasArchivos

@admin.register(Ponencia)
class PonenciasAdmin(admin.ModelAdmin):
    inlines = [PonenciasArchivosInline, ]




