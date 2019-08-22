from django.contrib import admin
from .models import Produto,Categoria,Unidade,Cliente,Fornecedor,Funcionario,FornecedorProduto

class FornecedorProdutoInline(admin.TabularInline):
    model= FornecedorProduto
    extra = 1

class ProdutoAdmin(admin.ModelAdmin):
    inlines = [FornecedorProdutoInline,]



admin.site.register([Categoria,Unidade,Cliente,Fornecedor,Funcionario])
admin.site.register(Produto,ProdutoAdmin)