from django.http import JsonResponse

def index(request):
    return JsonResponse({"message": "Examenes API funcionando correctamente."})
