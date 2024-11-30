from django.db import models


class Marca(models.Model):
    id = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=50, default="", verbose_name="Marca")
    logo = models.ImageField(upload_to='marcas/', null=True, blank=True, verbose_name="Logomarca")
    # revenda = models.CharField(max_length=50, null=True, blank=True, default="", verbose_name="Revenda")
    # cnpj = models.CharField(max_length=20, null=True, blank=True, default="", verbose_name="CNPJ")
    # endereco = models.CharField(max_length=100, null=True, blank=True, default="", verbose_name="Endereço")
    # numero = models.CharField(max_length=10, null=True, blank=True, default="", verbose_name="Nº")
    # complemento = models.CharField(max_length=50, null=True, blank=True, default="", verbose_name="Complemento")
    # bairro = models.CharField(max_length=50, null=True, blank=True, default="", verbose_name="Bairro")
    # cidade = models.CharField(max_length=50, null=True, blank=True, default="", verbose_name="Cidade")
    # uf = models.CharField(max_length=2, null=True, blank=True, default="", verbose_name="UF")
    # cep = models.CharField(max_length=10, null=True, blank=True, default="", verbose_name="CEP")
    # telefone = models.CharField(max_length=20, null=True, blank=True, default="", verbose_name="Telefone")
    # email = models.CharField(max_length=50, null=True, blank=True, default="", verbose_name="E-mail")

    class Meta:
        verbose_name_plural = "2.1- Marcas"
        verbose_name = "Marca"

    def __str__(self):
        return self.marca
