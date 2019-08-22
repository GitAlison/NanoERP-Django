from django.shortcuts import render
from django.views.generic import View
from sistema.cadastro.models import Cliente,Produto,Funcionario,Fornecedor
from sistema.pedido.models import Nota

# TODO index
class Index(View):
    def get(self,request):
        cliente = Cliente.objects.all().count()
        produto = Produto.objects.all().count()
        funcionario = Funcionario.objects.all().count()
        fornecedor = Fornecedor.objects.all().count()
        saidas = Nota.objects.all().count()
        entradas = Nota.objects.all().count()
        contexto ={
            'cliente':cliente,
            'funcionario':funcionario,
            'fornecedor':fornecedor,
            'produto':produto,
            'saida':saidas,
            'entrada':entradas,
        }
        template_neme = 'index.html'
        return render(request,template_neme,contexto)


class Caixa(View):
    def get(self,request):
        template_neme = 'caixa.html'
        return render(request,template_neme)
