from django.shortcuts import render
from .models import Producto
# Create your views here.

def home(request):
    productos = Producto.objects.all()
    return render(request, 'home.html', {'productos':productos})

def productos(request, id):
    producto = Producto.objects.get(id=id)
    return render(request, 'producto.html', {'producto':producto})