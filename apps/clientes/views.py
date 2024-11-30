from django.shortcuts import render, redirect, get_object_or_404
from apps.clientes.models import Cliente
from .forms import ClienteForm
from django.core.paginator import Paginator


def lista_clientes(request):
    clientes = Cliente.objects.all()
    paginator = Paginator(clientes, 10)
    page_number = request.GET.get('page')
    clientes = paginator.get_page(page_number)
    return render(request, 'clientes.html', {'clientes': clientes})


def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'editar_cliente.html', {'form': form})


def confirmar_exclusao(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, 'confirmar_exclusao.html', {'cliente': cliente})


def novo_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes')
    else:
        form = ClienteForm()
    return render(request, 'novo_cliente.html', {'form': form})


def excluir_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        cliente.delete()
        return redirect('clientes')
    return redirect('clientes')
