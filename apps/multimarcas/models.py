from django.db import models


class Periferico(models.Model):
    id = models.AutoField(primary_key=True)
    periferico = models.CharField(max_length=50, default="", verbose_name="Periférico")
    logo = models.ImageField(upload_to='perifericos/', null=True, blank=True, verbose_name="Logomarca")

    class Meta:
        verbose_name_plural = "3.1- Periféricos"
        verbose_name = "Periférico"

    def __str__(self):
        return self.periferico


class Grupo2(models.Model):
    id = models.AutoField(primary_key=True)
    idperiferico = models.ForeignKey(Periferico, on_delete=models.CASCADE, verbose_name="Grupo")
    grupo2 = models.CharField(max_length=50, default="", verbose_name="Grupo")

    class Meta:
        verbose_name_plural = "3.2- Grupos"
        verbose_name = "Grupo"

    def __str__(self):
        return self.grupo2  
    # return f"{self.idperiferico.periferico} - {self.grupo2}"


class Produto2(models.Model):
    id = models.AutoField(primary_key=True)
    idgrupo2 = models.ForeignKey(Grupo2, on_delete=models.CASCADE, verbose_name="Grupo")
    produto2 = models.CharField(max_length=50, default="", verbose_name="Produto")
    descricao = models.TextField(null=True, blank=True, verbose_name="Descrição")
    imagem = models.ImageField(upload_to='produtos/', null=True, blank=True, verbose_name="Imagem")
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Preço")

    class Meta:
        verbose_name_plural = "3.3- Produtos"
        verbose_name = "Produto"

    def __str__(self):
        return self.produto2
        # return f"{self.idgrupo2.grupo2} - {self.produto2}"
