from django.shortcuts import render, get_object_or_404
from apps.estoque.models import Marca, Grupo, Produto
from django.http import JsonResponse
from django.template.loader import render_to_string


def index(request):
    marcas = Marca.objects.all()
    return render(request, 'index.html', {'marcas': marcas})


def ajax_carregar_grupos(request):
    marca_id = request.GET.get('marca_id')
    grupos = Grupo.objects.filter(idmarca_id=marca_id).order_by('grupo')
    return render(request, 'grupo_dropdown_list_options.html', {'grupos': grupos})


def ajax_carregar_produtos(request):
    grupo_id = request.GET.get('grupo_id')
    produtos = Produto.objects.filter(idgrupo_id=grupo_id).order_by('produto')
    return render(request, 'produto_dropdown_list_options.html', {'produtos': produtos})


def ajax_obter_preco_produto(request):
    produto_id = request.GET.get('produto_id')
    produto = get_object_or_404(Produto, id=produto_id)
    data = {
        'preco': str(produto.preco)
    }
    return JsonResponse(data)
