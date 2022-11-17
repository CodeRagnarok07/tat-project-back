from django.contrib import admin

# Register your models here.
from .models import PreguntasFrecuente

from django_summernote.admin import SummernoteModelAdmin
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('text',)


admin.site.register(PreguntasFrecuente, PostAdmin)