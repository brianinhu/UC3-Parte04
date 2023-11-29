from django.shortcuts import render

# Create your views here.
def inicio(request):
    lista = ["LP3","Dibujo técnico","DBD", "Matemática II", "Gestión de Base de datos", "Filosofía", "Teoría de la Ciencia II"]
    return render(request, 'inicio.html',{'lista':lista}) 

