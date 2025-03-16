from django.http import JsonResponse

def index(request):
    return JsonResponse({"message": "Eventos API funcionando correctamente."})
