from django.urls import path
from .views import listar_pacientes, obtener_paciente, crear_paciente, obtener_reporte_completo

urlpatterns = [
    path('pacientes/', listar_pacientes, name='listar_pacientes'),
    path('pacientes/<int:paciente_id>/', obtener_paciente, name='obtener_paciente'),
    path('pacientes/crear/', crear_paciente, name='crear_paciente'),
    path('pacientes/<int:paciente_id>/reporte/', obtener_reporte_completo, name='obtener_reporte_completo'),
]
