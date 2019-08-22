from decimal import Decimal
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import Sum

class Pessoa(models.Model):
    TIPO_CHOICES = (
        ('J', 'Juridica'),
        ('F', 'Fisica'),
    )
    nome = models.CharField("Nome/Razão Social", max_length=100)

    tipo_pessoa = models.CharField('Tipo pessoa', max_length=4, choices=TIPO_CHOICES,
                                   null=True, blank=True)
    rg_ie = models.CharField('RG/IE', max_length=30, null=True, blank=True)
    cpf_cnpj = models.CharField('CPF/CNPJ', max_length=30, null=True, blank=True)

    #Contato
    fixo = models.CharField('Fixo',max_length=30,blank=True)
    whatsapp = models.CharField('Whatsapp',max_length=30,blank=True)
    celular = models.CharField('Celular',max_length=30,blank=True)
    trabalho = models.CharField('Trabalho',max_length=30,blank=True)

    #Endereço
    logradouro = models.CharField('Logradouro',max_length=80,blank=True)
    numero     = models.CharField('Numero',max_length=20,blank=True)
    bairro     = models.CharField('Bairro',max_length=80,blank=True)
    cidade     = models.CharField('Cidade',max_length=80,blank=True)
    uf = models.CharField('UF',max_length=80,blank=True)
    cep = models.CharField('CEP',max_length=80,blank=True)


    created_at = models.DateTimeField('Criado em', auto_now_add=True, blank=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['-id']

class Categoria(models.Model):
    nome = models.CharField('Gategoria', max_length=50)
    descricao = models.CharField('Descrição', max_length=50)

    created_at = models.DateTimeField('Criado em', auto_now_add=True, blank=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['-id']

class Unidade(models.Model):
    descricao = models.CharField('Descrição', max_length=50)
    sigla = models.CharField('Sigla', max_length=50)

    created_at = models.DateTimeField('Criado em', auto_now_add=True, blank=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True, blank=True)

    def __str__(self):
        return self.sigla

    class Meta:
        ordering = ['-id']

class Cliente(Pessoa):
    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['-id']


class Fornecedor(Pessoa):
    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['-id']


class Produto(models.Model):
    descricao = models.CharField("Descrição", max_length=100)
    preco = models.DecimalField('Preço', max_digits=10, decimal_places=2,
                                validators=[MinValueValidator(Decimal('0.00'))])
    custo = models.DecimalField('Custo', max_digits=10, decimal_places=2,
                                validators=[MinValueValidator(Decimal('0.00'))],
                                blank=True, null=True)
    categoria = models.ForeignKey(Categoria, related_name='categoria_produto',
                                  on_delete=models.CASCADE, blank=True, null=True)
    unidade = models.ForeignKey(Unidade, related_name='unidade_produto',
                                on_delete=models.CASCADE, blank=True, null=True)

    foto = models.ImageField('Foto Produto',
                             upload_to='produto/foto',
                             blank=True,
                             null=True,)
    cod_barras = models.CharField("Codigo de barras", max_length=100,blank=True)


    fora_de_linha = models.BooleanField('Fora de Linha', blank=True, default=False)
    controle_estoque = models.BooleanField('Controle de Estoque', blank=True, default=True)
    estoque_atual = models.DecimalField('Estoque Atual', max_digits=10, decimal_places=2,
                                validators=[MinValueValidator(Decimal('0.00'))],
                                blank=True, null=True,default=0)
    estoque_minimo = models.DecimalField('Estoque Minimo', max_digits=10, decimal_places=2,
                                        validators=[MinValueValidator(Decimal('0.00'))],
                                        blank=True, null=True,default=0)
    created_at = models.DateTimeField('Criado em', auto_now_add=True, blank=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True, blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.descricao


    def atualizaEstoqueAdd(self,quantidade):
        estoque = float(self.estoque_atual) + float(quantidade)
        self.estoque_atual = float(estoque)
        self.save()

    def atualizaEstoqueRemove(self,quantidade):
        estoque = float(self.estoque_atual) - float(quantidade)
        self.estoque_atual = float(estoque)
        self.save()

class Funcionario(Pessoa):
    data_nascimento = models.DateField('Nascimento', blank=True, null=True)
    data_admissao = models.DateField('Admissão', blank=True, null=True)
    data_demissao = models.DateField('Demissão', blank=True, null=True)
    salario = models.DecimalField('Salario', max_digits=10, decimal_places=2,
                                  validators=[MinValueValidator(Decimal('0.00'))])
    class Meta:
        ordering = ['-id']


class TipoPagamento(models.Model):

    descricao = models.CharField('Tipo Pagamento',max_length=20)
    created_at = models.DateTimeField('Criado Em', auto_now_add=True,blank=True )
    updated_at = models.DateTimeField('Atualizado em', auto_now=True,blank=True )

    def __str__(self):
        return self.descricao

class Pagamento(models.Model):
    STATUS_CHOICE = (
        (0,'Pago'),
        (1,'Pendente')
    )
    funcionario = models.ForeignKey(Funcionario,related_name='funcionario_pagamento',on_delete=models.CASCADE,blank=True, null=True)    
    tipo    = models.ForeignKey(TipoPagamento,related_name='tipo_tipopagamento', on_delete=models.CASCADE)
    valor   = models.DecimalField('Valor Pagamento',max_digits=10, decimal_places=2,validators=[MinValueValidator(Decimal('0.00'))])
    status  = models.IntegerField('Status',choices=STATUS_CHOICE) 
    observacaoes = models.TextField('Observacoes',blank=True, null=True)

    def __str__(self):
        return self.funcionario

class FornecedorProduto(models.Model):
    produto = models.ForeignKey(Produto,related_name='produto_fornecedor_produto',on_delete=models.CASCADE)
    fornecedor = models.ForeignKey(Fornecedor,related_name='fornecedor_produto',on_delete=models.CASCADE)
    unidade = models.ForeignKey(Unidade,related_name='unidade_fornecedor_produto',blank=True,null=True,on_delete=models.CASCADE)
    quantidade = models.DecimalField('Quantidade',decimal_places=3,max_digits=10,blank=True,null=True)

    def __str__(self):
        return str(self.produto)