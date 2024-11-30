from django.contrib import admin
from .models import Marca


# Register your models here.
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('marca', 'logo')
    # list_editable = ('logo')
    # search_fields = ('marca')
    list_per_page = 10


admin.site.register(Marca, MarcaAdmin)
