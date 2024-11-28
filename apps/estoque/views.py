from django.shortcuts import render
from apps.estoque.models import Marca


def index(request):
    marcas = Marca.objects.all()
    return render(request, 'index.html', {'marcas': marcas})
