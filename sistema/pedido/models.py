from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
from sistema.cadastro.models import Produto,Cliente,Funcionario,Fornecedor
from django.db.models import F,Sum,FloatField



#TODO Tipo Nota
class TipoNota(models.Model):
    descricao = models.CharField('Descricão',max_length=20)

    def __str__(self):
        return self.descricao


#TODO Nota
class Nota(models.Model):

    STATUS_CHOICES = (
        (0,'EMITIDA'),
        (1,'PENDENTE'),
        (2,'CANCELADA')
    )

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE,
                                    blank=True, null=True)
    tipo = models.ForeignKey(TipoNota,related_name='tipo_nota', on_delete=models.CASCADE)
    numero = models.CharField('Numero',max_length=20, blank=True, null=True)
    serie = models.CharField('Serie',max_length=20, blank=True, null=True)
    chave = models.CharField('Chave',max_length=1000, blank=True, null=True)

    status = models.CharField('STATUS',max_length=20, blank=True, null=True,choices=STATUS_CHOICES)

    data_emissao = models.DateField('Data de Emissão', blank=True, null=True)
    data_entrega = models.DateField('Data de Entrega', blank=True, null=True)
    status = models.CharField('STATUS',max_length=20, blank=True, null=True, choices=STATUS_CHOICES,default=1)

    total = models.DecimalField('Total do pedido',max_digits=10,decimal_places=2,
                                validators=[MinValueValidator(Decimal('0.00'))], blank=True,default=0, null=True)

    desconto = models.DecimalField('Desconto do pedido',max_digits=10,decimal_places=2,
                                validators=[MinValueValidator(Decimal('0.00'))], blank=True,default=0, null=True)

    despesa = models.DecimalField('Despesa do pedido', max_digits=10, decimal_places=2,
                                  validators=[MinValueValidator(Decimal('0.00'))], blank=True, default=0, null=True)

    created_at = models.DateTimeField('Criado em', auto_now_add=True, blank=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True, blank=True)

    def total_pedido(self):
        tot = self.itemnota_set.all().aggregate(tot=Sum(F('quantidade') * F('valor_unitario') - F('desconto_item'), output_field=FloatField()))['tot'] or 0

        total = tot + float(self.despesa or 0) - float(self.desconto or 0)
        self.total = float(total)
        self.save()

    def concluir_nota(self):

        # if self.tipo.descricao == 'Entrada':
        #     for item in self.itemnota_set.all():
        #         if item.produto.controle_estoque == True:
        #             item.produto.atualizaEstoqueAdd(item.quantidade)

        # elif self.tipo.descricao == 'Saida':
        #     for item in self.itemnota_set.all():
        #         if item.produto.controle_estoque == True:
        #             item.produto.atualizaEstoqueRemove(item.quantidade)

        self.status = 0
        self.save()

    def remover_nota(self):
        print('removendo Nota')
        if self.tipo.descricao == 'Entrada':
            for item in self.itemnota_set.all():
                if item.produto.controle_estoque == True:
                    item.produto.atualizaEstoqueRemove(item.quantidade)

        elif self.tipo.descricao == 'Saida':
            for item in self.itemnota_set.all():
                if item.produto.controle_estoque == True:
                    item.produto.atualizaEstoqueAdd(item.quantidade)

        self.status = 1
        self.save()





    def __str__(self):
        return str(self.id) +' '+ self.cliente.nome
    class Meta:
        ordering = ['-id']
        verbose_name = 'Nota'
        verbose_name_plural = 'Notas'

#TODO Item da Nota
class ItemNota(models.Model):
    nota = models.ForeignKey(Nota,on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto,on_delete=models.CASCADE)
    quantidade = models.DecimalField('Quantidade',max_digits=10,decimal_places=2,
                                     validators=[MinValueValidator(Decimal('0.00'))]
                                     )
    valor_unitario = models.DecimalField('Valor Unit.',max_digits=10,decimal_places=2,
                                     validators=[MinValueValidator(Decimal('0.00'))],blank=True,default=0)
    desconto_item= models.DecimalField('Desconto', max_digits=10, decimal_places=2,
                                         validators=[MinValueValidator(Decimal('0.00'))],
                                  blank=True,default=0)
    total_item = models.DecimalField('Total Item', max_digits=10, decimal_places=2,
                                   validators=[MinValueValidator(Decimal('0.00'))], blank=True,default=0)

    created_at = models.DateTimeField('Criado em', auto_now_add=True, blank=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True, blank=True)

    class Meta:
        ordering = ['-id']







