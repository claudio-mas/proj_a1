# Generated by Django 5.0.9 on 2024-11-30 21:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Periferico',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('periferico', models.CharField(default='', max_length=50, verbose_name='Periferico')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='perifericos/', verbose_name='Logomarca')),
            ],
            options={
                'verbose_name': 'Periférico',
                'verbose_name_plural': '3.1- Periféricos',
            },
        ),
        migrations.CreateModel(
            name='Grupo2',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('grupo2', models.CharField(default='', max_length=50, verbose_name='Grupo')),
                ('idperiferico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='multimarcas.periferico', verbose_name='Periférico')),
            ],
            options={
                'verbose_name': 'Grupo',
                'verbose_name_plural': '3.2- Grupos',
            },
        ),
        migrations.CreateModel(
            name='Produto2',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('produto2', models.CharField(default='', max_length=50, verbose_name='Produto')),
                ('descricao', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='produtos/', verbose_name='Imagem')),
                ('preco', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Preço')),
                ('idgrupo2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='multimarcas.grupo2', verbose_name='Grupo')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': '3.3- Produtos',
            },
        ),
    ]
