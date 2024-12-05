from django.db import models
from django.utils import timezone
from apps.estoque.models import Marca, Grupo


class Orcamento(models.Model):
    TIPO_STATUS = (
        ('Em Andamento', 'Em Andamento'),
        ('Aprovado', 'Aprovado'),
        ('Reprovado', 'Reprovado'),
        ('Cancelado', 'Cancelado'),
    )
    id = models.AutoField(primary_key=True)
    data = models.DateField(blank=True, null=True, default=timezone.now, verbose_name="Data")
    numero = models.CharField(max_length=10, verbose_name="Nº Orçamento")
    idcliente = models.ForeignKey('clientes.Cliente', on_delete=models.CASCADE, verbose_name="Cliente")
    descricao = models.TextField(blank=True, null=True, verbose_name="Observações")
    validade = models.DateField(blank=True, null=True, verbose_name='Validade')
    total = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2, verbose_name="Valor Total")
    status = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        default='Em Andamento',
        choices=TIPO_STATUS,
        verbose_name='Status'
    )

    def atualizar_total(self):
        total = self.orcamentoitem_set.aggregate(total=models.Sum('subtotal'))['total'] or 0
        self.total = total
        self.save()

    class Meta:
        verbose_name_plural = "4.1- Orçamentos"
        verbose_name = "Orçamento"

    def __str__(self):
        return self.numero


class OrcamentoItem(models.Model):
    id = models.AutoField(primary_key=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, verbose_name="Marca", null=True, blank=True)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, verbose_name="Grupo", null=True, blank=True)
    idorcamento = models.ForeignKey(Orcamento, on_delete=models.CASCADE, verbose_name="Orçamento")
    idproduto = models.ForeignKey('estoque.Produto', on_delete=models.CASCADE, blank=True, null=True, verbose_name="Produto")
    idproduto2 = models.ForeignKey('multimarcas.Produto2', on_delete=models.CASCADE, blank=True, null=True, verbose_name="Periférico")
    quantidade = models.IntegerField(verbose_name="Quantidade", default=1)
    valor = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço Unit.", blank=True, null=True, default=0)
    desconto = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Desconto", blank=True, null=True, default=0)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Subtotal", blank=True, null=True, default=0)

    class Meta:
        verbose_name_plural = "4.2- Itens do Orçamento"
        verbose_name = "Itens do Orçamento"

    def __str__(self):
        produto_nome = self.idproduto.produto if self.idproduto else 'Sem Produto'
        return f"{self.idorcamento.numero} - {produto_nome}"
