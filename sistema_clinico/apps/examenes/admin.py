from django.contrib import admin
from .models import Examen


@admin.register(Examen)
class ExamenAdmin(admin.ModelAdmin):
    list_display = ("id", "paciente", "tipo", "get_resultado", "get_fecha_realizacion", "medico")
    list_filter = ("tipo",)
    search_fields = ("paciente_nombre", "tipo")

    def get_resultado(self, obj):
        return obj.resultado if hasattr(obj, "resultado") else "No disponible"

    get_resultado.short_description = "Resultado"

    def get_fecha_realizacion(self, obj):
        return (
            obj.fecha_realizacion
            if hasattr(obj, "fecha_realizacion")
            else "No disponible"
        )

    get_fecha_realizacion.admin_order_field = "fecha_realizacion"
    get_fecha_realizacion.short_description = "Fecha de realización"
    