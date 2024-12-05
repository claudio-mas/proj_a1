# Generated by Django 5.0.9 on 2024-12-05 00:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0004_alter_produto_preco'),
        ('orcamentos', '0003_alter_orcamentoitem_desconto_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orcamentoitem',
            name='grupo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='estoque.grupo', verbose_name='Grupo'),
        ),
        migrations.AddField(
            model_name='orcamentoitem',
            name='marca',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='estoque.marca', verbose_name='Marca'),
        ),
    ]
