from django.shortcuts import render
from .models import Servicio

def lista_servicios(request):
    servicios = Servicio.objects.all()
    context = {'servicios': servicios}
    return render(request, 'lista_servicios.html', context)

def nuestros_servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'nuestros_servicios.html', {'servicios': servicios})