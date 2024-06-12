from django.shortcuts import render
from .models import Producto, Categoria
# Create your views here.



def index(request):
    producto= Producto.objects.all()
    context={"producto":producto}
    return render(request, 'index.html', context)

def listadoSQL(request):
    producto= Producto.objects.raw('SELECT * FROM categoria_Producto')
    print(producto)
    context={"producto":producto}
    return render(request, 'listadoSQL.html', context)