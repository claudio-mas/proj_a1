from django.contrib import admin
from .models import Marca, Grupo, Produto
from django.utils.html import format_html


# Register your models here.
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('marca', 'logo')
    # list_editable = ('logo')
    # search_fields = ('marca')
    list_per_page = 10


class GrupoAdmin(admin.ModelAdmin):
    list_display = ('grupo', 'idmarca')
    # list_editable = ('grupo')
    # search_fields = ('grupo')


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('produto', 'idgrupo', 'preco_formatado', 'imagem')
    # list_editable = ('preco_formatado', 'imagem')
    search_fields = ('produto', 'marca')

    def preco_formatado(self, obj):
        if obj.preco is None:
            return "R$ 0,00"
        return f"R$ {obj.preco:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    preco_formatado.short_description = "Preço"


admin.site.register(Marca, MarcaAdmin)
admin.site.register(Grupo, GrupoAdmin)
admin.site.register(Produto, ProdutoAdmin)
