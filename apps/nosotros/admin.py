from django.contrib import admin

# Register your models here.
from .models import Oficina, Departamento, Autoridad, Equipo
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('text',)



admin.site.register(Oficina)
admin.site.register(Departamento)

# admin.site.register(Autoridad, PostAdmin)


admin.site.register(Equipo, PostAdmin)


@admin.register(Autoridad)
class ArutoridadAdmin(SummernoteModelAdmin):
    readonly_fields = ('slug',)
    summernote_fields = ['text', ]
    # inlines = [SeccionInline, ]
    # autocomplete_fields = ['']
    # def get_search_results(self, request, queryset, search_term):
    #     print("In get search results")
    #     results = super().get_search_results(request, queryset, search_term)
    #     return results
