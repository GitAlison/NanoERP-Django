# Generated by Django 2.2 on 2019-02-01 23:34

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0007_pagamento_tipopagamento'),
        ('pedido', '0005_auto_20180819_0242'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemNota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='Quantidade')),
                ('valor_unitario', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='Valor Unit.')),
                ('desconto_item', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='Desconto')),
                ('total_item', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='Total Item')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_emissao', models.DateField(blank=True, null=True, verbose_name='Data de Emissão')),
                ('data_entrega', models.DateField(blank=True, null=True, verbose_name='Data de Entrega')),
                ('status', models.CharField(blank=True, choices=[('EMITIDA', 'EMITIDA'), ('PENDENTE', 'PENDENTE'), ('CENCELADA', 'CANCELADA')], max_length=20, null=True, verbose_name='STATUS')),
                ('total', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='Total do pedido')),
                ('desconto', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='Desconto do pedido')),
                ('despesa', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='Despesa do pedido')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.Cliente')),
                ('funcionario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cadastro.Funcionario')),
            ],
            options={
                'verbose_name': 'Nota',
                'verbose_name_plural': 'Notas',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='TipoNota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=20, verbose_name='Descricão')),
            ],
        ),
        migrations.RemoveField(
            model_name='itementrada',
            name='entrada',
        ),
        migrations.RemoveField(
            model_name='itementrada',
            name='produto',
        ),
        migrations.RemoveField(
            model_name='itemsaida',
            name='produto',
        ),
        migrations.RemoveField(
            model_name='itemsaida',
            name='saida',
        ),
        migrations.RemoveField(
            model_name='saida',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='saida',
            name='funcionario',
        ),
        migrations.DeleteModel(
            name='Entrada',
        ),
        migrations.DeleteModel(
            name='ItemEntrada',
        ),
        migrations.DeleteModel(
            name='ItemSaida',
        ),
        migrations.DeleteModel(
            name='Saida',
        ),
        migrations.AddField(
            model_name='nota',
            name='tipo_nota',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tipo_nota', to='pedido.TipoNota'),
        ),
        migrations.AddField(
            model_name='itemnota',
            name='nota',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedido.Nota'),
        ),
        migrations.AddField(
            model_name='itemnota',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.Produto'),
        ),
    ]
