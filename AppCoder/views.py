from django.http import HttpResponse
from django.shortcuts import render

from django.http import HttpResponse
from .models import Curso 

# Create your views here.

def crear_curso (resquest,camada):
    curso = Curso(nombre='Python', camada=camada)
    curso.save()
    return HttpResponse(f'Curso creado! {camada}')