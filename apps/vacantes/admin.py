from django.contrib import admin

# Register your models here.
from .models import Vacante
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('requisitos',)


admin.site.register(Vacante, PostAdmin)