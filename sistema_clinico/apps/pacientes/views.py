from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Paciente
from sistema_clinico.apps.eventos.models import Evento
from sistema_clinico.apps.examenes.models import Examen
import json
from django.views.decorators.csrf import csrf_exempt


def obtener_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    return JsonResponse(
        {
            "id": paciente.id,
            "nombre": paciente.nombre,
            "cc": paciente.cc,
            "edad": paciente.edad,
            "genero": paciente.genero,
        }
    )


def listar_pacientes(request):
    pacientes = list(Paciente.objects.values())
    return JsonResponse(pacientes, safe=False)


def obtener_reporte_completo(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)

    eventos = Evento.objects.filter(paciente_id=paciente.id)

    return JsonResponse(
        {
            "paciente": {
                "id": paciente.id,
                "nombre": paciente.nombre,
                "cc": paciente.cc,
                "edad": paciente.edad,
                "genero": paciente.genero,
            },
            "eventos": list(eventos.values("id", "descripcion", "fecha")),
        }
    )


@csrf_exempt
def crear_paciente(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            paciente = Paciente.objects.create(
                nombre=data["nombre"],
                cc=data["cc"],
                edad=data["edad"],
                genero=data["genero"],
            )
            return JsonResponse(
                {"id": paciente.id, "mensaje": "Paciente creado correctamente"},
                status=201,
            )
        except KeyError as e:
            return JsonResponse({"error": f"Falta el campo {str(e)}"}, status=400)
    else:
        return JsonResponse({"error": "Método no permitido"}, status=405)
