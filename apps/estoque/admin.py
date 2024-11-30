from django.contrib import admin
from .models import Marca, Grupo, Produto


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
    list_display = ('produto', 'idgrupo', 'preco', 'imagem')
    list_editable = ('preco', 'imagem')
    search_fields = ('produto', 'marca')


admin.site.register(Marca, MarcaAdmin)
admin.site.register(Grupo, GrupoAdmin)
admin.site.register(Produto, ProdutoAdmin)
