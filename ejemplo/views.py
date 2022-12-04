from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "ejemplo/saludar.html")


def saludar_a(request, nombre):
    return render(request,
    "ejemplo/saludar_a.html",
    {"nombre": nombre}
    )

def sumar(request, a, b):
    return render(request,
    "ejemplo/sumar.html",
    {"a": a, "b": b, "resultado": a + b})


def buscar(request):
    lista_de_nombre = ['Rodrigo', 'Tomas', 'Nicolas', 'Santiago', 'Silvina']
    query = request.GET['q']

    if query in lista_de_nombre:
        indice_de_resultado = lista_de_nombre.index(query)
        resultado = lista_de_nombre[indice_de_resultado]

    else:
        resultado = 'no hay match'

    return render(request, 'ejemplo/buscar.html', {'resultado': resultado})







