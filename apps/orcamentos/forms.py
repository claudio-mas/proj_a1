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
        exclude = ['idorcamento', 'subtotal']
        widgets = {
            'idproduto': forms.Select(attrs={'class': 'form-control'}),
            'idproduto2': forms.Select(attrs={'class': 'form-control'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control'}),
            'desconto': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        idproduto = cleaned_data.get('idproduto')
        idproduto2 = cleaned_data.get('idproduto2')

        if idproduto and idproduto2:
            raise forms.ValidationError("Selecione apenas um: Produto ou Periférico, não ambos.")
        if not idproduto and not idproduto2:
            raise forms.ValidationError("Você deve selecionar um Produto ou um Periférico.")

        return cleaned_data
