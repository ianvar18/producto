from django.shortcuts import render
from .models import Producto, Categoria
# Create your views here.



def index(request):
    producto= Producto.objects.all()
    context={"producto":producto}
    return render(request, 'index.html', context)