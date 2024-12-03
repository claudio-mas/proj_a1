from django import forms
from .models import Orcamento, OrcamentoItem


class OrcamentoForm(forms.ModelForm):
    class Meta:
        model = Orcamento
        fields = ['id', 'numero', 'data', 'idcliente', 'descricao', 'validade', 'total', 'status']
        widgets = {
            'data': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'validade': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }


class OrcamentoItemForm(forms.ModelForm):
    class Meta:
        model = OrcamentoItem
        fields = ['id', 'idproduto', 'idproduto2', 'quantidade', 'valor', 'desconto']

        widgets = {
            'idproduto': forms.Select(attrs={'class': 'form-control'}),
            'idproduto2': forms.Select(attrs={'class': 'form-control'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control'}),
            'desconto': forms.NumberInput(attrs={'class': 'form-control'}),
        }
