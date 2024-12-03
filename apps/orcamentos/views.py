from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView
from .models import Orcamento, OrcamentoItem
from .forms import OrcamentoForm, OrcamentoItemForm


# def lista_orcamentos(request):
#     orcamentos = Orcamento.objects.all()
#     return render(request, 'orcamentos_lista.html', {'orcamentos': orcamentos})


def format_currency_value(amount):
    return f"R$ {amount:,.2f}".replace('.', ',')


def lista_orcamentos(request):
    # Buscar os orçamentos do banco de dados
    orcamentos = Orcamento.objects.all()

    # Formatar os dados para exibição no template
    orcamentos_formatados = []
    for orcamento in orcamentos:
        orcamentos_formatados.append({
            'id': orcamento.id,
            'numero': orcamento.numero,
            'data': orcamento.data.strftime('%d/%m/%Y'),  # Formata a data
            'idcliente': orcamento.idcliente,
            'descricao': orcamento.descricao,
            'validade': orcamento.validade.strftime('%d/%m/%Y'),  # Formata a validade
            'total': format_currency_value(orcamento.total),  # Formata o valor total
            'status': orcamento.status
        })

    # Renderizar o template com os dados formatados
    return render(request, 'orcamentos_lista.html', {'orcamentos': orcamentos_formatados})


def editar_orcamento(request, id):
    orcamento = get_object_or_404(Orcamento, id=id)
    if request.method == 'POST':
        form = OrcamentoForm(request.POST, instance=orcamento)
        if form.is_valid():
            form.save()
            return redirect('lista_orcamentos')
    else:
        form = OrcamentoForm(instance=orcamento)
    # Passando 'orcamento' no contexto
    return render(request, 'orcamento_editar.html', {'form': form, 'orcamento': orcamento})


def excluir_orcamento(request, id):
    orcamento = get_object_or_404(Orcamento, id=id)
    if request.method == 'POST':
        orcamento.delete()
        return redirect('lista_orcamentos')
    return render(request, 'orcamento_confirmar_exclusao.html', {'orcamento': orcamento})


def adicionar_item_orcamento(request, orcamento_id):
    orcamento = get_object_or_404(Orcamento, id=orcamento_id)
    if request.method == 'POST':
        form = OrcamentoItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.idorcamento = orcamento  # Associa o item ao orçamento
            try:
                # Calcula o subtotal
                item.subtotal = (item.valor * item.quantidade) - item.desconto
                item.save()
                return redirect('detalhar_orcamento', orcamento_id=orcamento.id)
            except Exception as e:
                form.add_error(None, f"Ocorreu um erro ao salvar o item: {e}")
        else:
            print(form.errors)  # Imprime os erros do formulário no console
    else:
        form = OrcamentoItemForm()
    return render(request, 'adicionar_item_orcamento.html', {'form': form, 'orcamento': orcamento})


def detalhar_orcamento(request, orcamento_id):
    orcamento = get_object_or_404(Orcamento, id=orcamento_id)
    itens = OrcamentoItem.objects.filter(idorcamento=orcamento)
    return render(request, 'detalhar_orcamento.html', {'orcamento': orcamento, 'itens': itens})


class OrcamentoCreateView(CreateView):
    model = Orcamento
    form_class = OrcamentoForm
    template_name = 'orcamento_form.html'

    def form_valid(self, form):
        form.save()
        return redirect('lista_orcamentos')
