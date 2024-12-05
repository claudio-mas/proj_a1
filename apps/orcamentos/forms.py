from django import forms
from .models import Orcamento, OrcamentoItem
from apps.estoque.models import Marca, Grupo, Produto


class OrcamentoForm(forms.ModelForm):
    class Meta:
        model = Orcamento
        fields = ['id', 'numero', 'data', 'idcliente', 'descricao', 'validade', 'total', 'status']
        widgets = {
            'data': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'validade': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }

        def __init__(self, *args, **kwargs):
            super(OrcamentoForm, self).__init__(*args, **kwargs)
            self.fields['descricao'].widget.attrs.update({'style': 'height: 20px;'}) 


class OrcamentoItemForm(forms.ModelForm):
    marca = forms.ModelChoiceField(
        queryset=Marca.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True
    )
    grupo = forms.ModelChoiceField(
        queryset=Grupo.objects.none(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True
    )
    idproduto = forms.ModelChoiceField(
        queryset=Produto.objects.none(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True,
        label="Produto"
    )

    class Meta:
        model = OrcamentoItem
        exclude = ['idorcamento', 'subtotal']
        widgets = {
            'marca': forms.Select(attrs={'class': 'form-control'}),
            'grupo': forms.Select(attrs={'class': 'form-control'}),
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

    def __init__(self, *args, **kwargs):
        super(OrcamentoItemForm, self).__init__(*args, **kwargs)
        if 'marca' in self.data:
            try:
                marca_id = int(self.data.get('marca'))
                self.fields['grupo'].queryset = Grupo.objects.filter(idmarca_id=marca_id).order_by('grupo')
            except (ValueError, TypeError):
                self.fields['grupo'].queryset = Grupo.objects.none()
        elif self.instance.pk:
            if self.instance.marca:
                self.fields['grupo'].queryset = Grupo.objects.filter(idmarca=self.instance.marca).order_by('grupo')
            else:
                self.fields['grupo'].queryset = Grupo.objects.none()
        else:
            self.fields['grupo'].queryset = Grupo.objects.none()

        if 'grupo' in self.data:
            try:
                grupo_id = int(self.data.get('grupo'))
                self.fields['idproduto'].queryset = Produto.objects.filter(idgrupo_id=grupo_id).order_by('produto')
            except (ValueError, TypeError):
                self.fields['idproduto'].queryset = Produto.objects.none()
        elif self.instance.pk:
            if self.instance.grupo:
                self.fields['idproduto'].queryset = Produto.objects.filter(idgrupo=self.instance.grupo).order_by('produto')
            else:
                self.fields['idproduto'].queryset = Produto.objects.none()
        else:
            self.fields['idproduto'].queryset = Produto.objects.none()
