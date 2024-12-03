from django import forms
from .models import Orcamento


class OrcamentoForm(forms.ModelForm):
    class Meta:
        model = Orcamento
        fields = ['id', 'numero', 'data', 'idcliente', 'descricao', 'validade', 'total', 'status']
        widgets = {
            'data': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'validade': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }
