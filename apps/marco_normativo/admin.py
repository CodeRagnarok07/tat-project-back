from django.contrib import admin

# Register your models here.
from .models import Competencia, LeyesYDecreto, Acuerdo,Convenio, Edicto, Flujograma
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('text',)


admin.site.register(Competencia, PostAdmin)
admin.site.register(Acuerdo)
admin.site.register(Convenio)
admin.site.register(Edicto)
admin.site.register(Flujograma)
admin.site.register(LeyesYDecreto)