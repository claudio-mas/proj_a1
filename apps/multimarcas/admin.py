from django.contrib import admin
from .models import Periferico, Grupo2, Produto2
from django.utils.html import format_html


# Register your models here.
class PerifericoAdmin(admin.ModelAdmin):
    list_display = ('periferico', 'logo')
    # list_editable = ('periferico')
    list_per_page = 10


class Grupo2Admin(admin.ModelAdmin):
    list_display = ('grupo2', 'idperiferico')
    # list_editable = ('grupo2')
# search_fields = ('grupo2')


class Produto2Admin(admin.ModelAdmin):
    list_display = ('produto2', 'idgrupo2', 'preco_formatado', 'imagem')
    # list_editable = ('preco_formatado', 'imagem')
    search_fields = ('produto2', 'periferico')

    def preco_formatado(self, obj):
        if obj.preco is None:
            return "R$ 0,00"
        return f"R$ {obj.preco:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    preco_formatado.short_description = "Preço"


admin.site.register(Periferico, PerifericoAdmin)
admin.site.register(Grupo2, Grupo2Admin)
admin.site.register(Produto2, Produto2Admin)
