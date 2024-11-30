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


class Grupo(models.Model):
    id = models.AutoField(primary_key=True)
    idmarca = models.ForeignKey(Marca, on_delete=models.CASCADE, verbose_name="Marca")
    grupo = models.CharField(max_length=50, default="", verbose_name="Grupo")

    class Meta:
        verbose_name_plural = "2.2- Grupos"
        verbose_name = "Grupo"

    def __str__(self):
        return self.grupo


class Produto(models.Model):
    id = models.AutoField(primary_key=True)
    idgrupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, verbose_name="Grupo")
    produto = models.CharField(max_length=50, default="", verbose_name="Produto")
    descricao = models.TextField(null=True, blank=True, verbose_name="Descrição")
    imagem = models.ImageField(upload_to='produtos/', null=True, blank=True, verbose_name="Imagem")
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Preço")

    class Meta:
        verbose_name_plural = "2.3- Produtos"
        verbose_name = "Produto"

    def __str__(self):
        return self.produto
