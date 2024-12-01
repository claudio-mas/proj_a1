from django.contrib import admin
from .models import Orcamento, OrcamentoItem


class OrcamentoAdmin(admin.ModelAdmin):
    list_display = ('idcliente', 'numero', 'data', 'valor_total_formatado')
    # list_editable = ('data', 'valor_total_formatado')
    search_fields = ('idcliente', 'data')
    list_per_page = 10

    def valor_total_formatado(self, obj):
        if obj.total is None:
            return "R$ 0,00"
        return f"R$ {obj.total:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    valor_total_formatado.short_description = "Valor Total"


class OrcamentoItemAdmin(admin.ModelAdmin):
    list_display = ('idorcamento', 'idproduto', 'quantidade', 'preco_formatado')
    # list_editable = ('quantidade', 'preco_formatado')
    search_fields = ('orcamento', 'produto', 'quantidade', 'preco_formatado')
    list_per_page = 10

    def preco_formatado(self, obj):
        if obj.preco is None:
            return "R$ 0,00"
        return f"R$ {obj.preco:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    preco_formatado.short_description = "Preço"


admin.site.register(Orcamento, OrcamentoAdmin)
admin.site.register(OrcamentoItem, OrcamentoItemAdmin)
