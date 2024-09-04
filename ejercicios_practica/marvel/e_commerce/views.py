from django.shortcuts import render
from django.http import JsonResponse
from django.urls import path

# Create your views here.
def hola_mundo(request):    
    datos =  {"mensaje": "hola_mundo", "curso": "python-django"}
    return JsonResponse(datos)

def get_comic_api_view(request):
    print("Endpoint get_comic_api_view")
    # Alumno, aquí deberá completar el endpoint
    comic_data = {
        "id": 1,
        "marvel_comic": "1010",
        "title": "Inove",
        "stock_qty": 6,
        "description": "Mi primer JSON en Django",
        "price": 10.0,
        "picture": "https://www.django-rest-framework.org/img/logo.png"
    }
    
    # Retornar los datos como JSON
    return JsonResponse(comic_data)

