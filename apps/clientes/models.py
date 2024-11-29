from django.db import models


class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=150, unique=True, verbose_name="Nome")
    cpf = models.CharField(max_length=14, unique=True, null=True, blank=True, default="", verbose_name="CPF")
    rg = models.CharField(max_length=12, unique=True, null=True, blank=True, default="", verbose_name="RG")
    cnpj = models.CharField(max_length=20, unique=True, null=True, blank=True, default="", verbose_name="CNPJ")
    cro = models.CharField(max_length=10, unique=True, null=True, blank=True,default="", verbose_name="CRO")
    datanasc = models.DateField(null=True, blank=True, verbose_name="Data de Nascimento")
    endereco = models.CharField(max_length=100, null=True, blank=True, default="", verbose_name="Endereço")
    numero = models.CharField(max_length=10, null=True, blank=True, default="", verbose_name="Nº")
    complemento = models.CharField(max_length=50, null=True, blank=True, default="")
    bairro = models.CharField(max_length=50, null=True, blank=True)
    cidade = models.CharField(max_length=50, null=True, blank=True)
    uf = models.CharField(max_length=2, null=True, blank=True, default="", verbose_name="UF")
    cep = models.CharField(max_length=10, null=True, blank=True, default="", verbose_name="CEP")
    telefone = models.CharField(max_length=20, null=True, blank=True, default="", verbose_name="Telefone")
    celular = models.CharField(max_length=20, null=True, blank=True, default="", verbose_name="Celular")
    whatsapp = models.BooleanField()
    email = models.EmailField(blank=True, null=True, default="", verbose_name="E-mail")
    instagram = models.CharField(max_length=50, null=True, blank=True, default="", verbose_name="Instagram")

    class Meta:
        verbose_name_plural = "1.1- Cadastro"
        verbose_name = "Cliente"

    def __str__(self):
        return self.nome
