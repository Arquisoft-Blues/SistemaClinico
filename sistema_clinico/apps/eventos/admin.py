from django.contrib import admin
from .models import Evento

@admin.register(Evento)
class EventoClinicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'paciente', 'descripcion', 'fecha')
    search_fields = ('paciente__nombre', 'descripcion')
