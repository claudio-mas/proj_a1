from django import forms
from .models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        # fields = ['Nome', 'CPF', 'RG', 'DataNasc', 'CNPJ', 'CRO', 'Endereco', 'Numero', 'Complemento', 'Bairro', 'Cidade', 'UF', 'CEP', 'Telefone', 'Celular', 'Whatsapp', 'Email', 'Instagram']
        fields = '__all__'
        widgets = {
            'Nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome completo'}),
            'CPF': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 000.000.000-00', 'id': 'id_CPF'}),
            'Email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@exemplo.com'}),
            'Celular': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: (00) 00000-0000'}),
            # Adicione widgets para os outros campos
            'RG': forms.TextInput(attrs={'class': 'form-control'}),
            'DataNasc': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'CNPJ': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 00.000.000/0000-00'}),
            'CRO': forms.TextInput(attrs={'class': 'form-control'}),
            'Endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'Numero': forms.TextInput(attrs={'class': 'form-control'}),
            'Complemento': forms.TextInput(attrs={'class': 'form-control'}),
            'Bairro': forms.TextInput(attrs={'class': 'form-control'}),
            'Cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'UF': forms.TextInput(attrs={'class': 'form-control'}),
            'CEP': forms.TextInput(attrs={'class': 'form-control'}),
            'Telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: (00) 0000-0000'}),
            'Whatsapp': forms.CheckboxInput(),
            'Instagram': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'Nome': 'Nome',
            'CPF': 'CPF',
            'RG': 'RG',
            'DataNasc': 'Data de Nascimento',
            'CNPJ': 'CNPJ',
            'CRO': 'CRO',
            'Endereco': 'Logradouro',
            'Numero': 'Nº',
            'Complemento': 'Complemento',
            'Bairro': 'Bairro',
            'Cidade': 'Cidade',
            'UF': 'UF',
            'CEP': 'CEP',
            'Telefone': 'Telefone',
            'Celular': 'Celular',
            'Whatsapp': 'Whatsapp',
            'Email': 'E-mail',
            'Instagram': 'Instagram',
        }
