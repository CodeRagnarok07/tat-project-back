from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin, SummernoteInlineModelAdmin

from .models import Pagina, Seccion, Contenido
# Register your models here.


class ContenidoInline(admin.StackedInline, SummernoteInlineModelAdmin):
    extra = 1
    model = Contenido
    summernote_fields = ['text', ]
    fieldsets = (
        (None, {
            'classes': ('extrapretty',),
            'fields': ('titulo','posicion')
        }),
        ("icono", {
            'classes': ('extrapretty', 'collapse'),
            'fields': (('icono', ),)
        }),
        ("text", {
            'classes': ('extrapretty', 'collapse'),
            'fields': (('text', ),)
        }),
    )


class SeccionInline(admin.StackedInline,SummernoteInlineModelAdmin):
    extra = 1
    model = Seccion
    inlines = [ContenidoInline, ]
    summernote_fields = ['text', ]

    fieldsets = (
        (None, {
            'classes': ('extrapretty',),
            'fields': ('titulo', 'imagen', 'posicion')
        }),
        ("icono", {
            'classes': ('extrapretty', 'collapse'),
            'fields': (('icono', ),)
        }),
        ("text", {
            'classes': ('extrapretty', 'collapse'),
            'fields': (('text', ),)
        }),
    )


@admin.register(Seccion)
class SeccionAdmin(SummernoteModelAdmin):
    list_display = ('titulo', 'posicion', 'pagina', )
    search_fields = ['titulo']
    list_filter = ('pagina__titulo_pagina',)
    summernote_fields = ['text', ]
    fieldsets = (
        (None, {
            'classes': ('extrapretty',),
            'fields': ('titulo', 'imagen', 'posicion')
        }),
        ("icono", {
            'classes': ('extrapretty', 'collapse'),
            'fields': (('icono', ),)
        }),
        ("text", {
            'classes': ('extrapretty', 'collapse'),
            'fields': (('text', ),)
        }),
    )

    inlines = [ContenidoInline, ]


@admin.register(Pagina)
class PaginaAdmin(SummernoteModelAdmin):
    list_display = ('titulo_pagina', )
    search_fields = ['titulo']
    readonly_fields = ('titulo_pagina',)
    # summernote_fields = ['descripcion', ]
    inlines = [SeccionInline, ]

    # autocomplete_fields = ['']
    # def get_search_results(self, request, queryset, search_term):
    #     print("In get search results")
    #     results = super().get_search_results(request, queryset, search_term)
    #     return results
