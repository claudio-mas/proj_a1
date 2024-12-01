from django.shortcuts import render
from .models import Orcamento


def lista_orcamentos(request):
    orcamentos = Orcamento.objects.all()
    return render(request, 'orcamentos_lista.html', {'orcamentos': orcamentos})
