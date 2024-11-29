from django.contrib import admin
from .models import Cliente


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'rg', 'cnpj', 'cro')
    list_editable = ('cpf', 'rg', 'cnpj', 'cro')
    search_fields = ('nome', 'cpf', 'rg', 'cnpj', 'cro')


admin.site.register(Cliente, ClienteAdmin)
