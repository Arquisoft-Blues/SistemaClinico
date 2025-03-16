from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/reportes/', include('sistema_clinico.apps.reportes.urls')),
    path('api/examenes/', include('sistema_clinico.apps.examenes.urls')),
    path('api/eventos/', include('sistema_clinico.apps.eventos.urls')),
]
