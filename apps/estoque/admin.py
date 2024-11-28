from django.contrib import admin
from .models import Marca


# Register your models here.
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('marca', 'logo', 'revenda')
    list_editable = ('logo', 'revenda')
    search_fields = ('marca', 'revenda')
    list_per_page = 10


admin.site.register(Marca, MarcaAdmin)
