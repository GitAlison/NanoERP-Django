from django.shortcuts import render,redirect,get_object_or_404,HttpResponse,HttpResponseRedirect
from django.urls import reverse_lazy,reverse
from django.views.generic import View,ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView
from django.contrib import messages
from .models import Nota,ItemNota
from .forms import NotaForm,ItemNotaForm


class Saidas(ListView):
    model = Nota
    queryset = Nota.objects.filter(tipo__descricao='Saida')
    def get_context_data(self, **kwargs):
        context = super(Saidas,self).get_context_data(**kwargs)
        context['tipo_relatorio'] = 'Saidas'
        return context
    
class Entradas(ListView):
    model = Nota
    queryset = Nota.objects.filter(tipo__descricao='Entrada')
    def get_context_data(self, **kwargs):
        context = super(Entradas,self).get_context_data(**kwargs)
        context['tipo_relatorio'] = 'Entradas'
        return context

class NotaCreate(CreateView):
    model = Nota
    form_class = NotaForm

    def get_success_url(self):
        return reverse_lazy('pedido:nota-update', kwargs={'pk': self.object.pk})

class NotaRemove(View):
    def get(self,request,pk):
        saida = Nota.objects.get(pk=pk)
        saida.remover_nota()
        saida.delete()
        messages.success(request,'Movimento saida N°'+str(pk)+' apagado ')
        return redirect('pedido:saida-list')

class NotaUpdate(UpdateView):
    model = Nota
    form_class = NotaForm
    def get_context_data(self, **kwargs):
        context = super(NotaUpdate,self).get_context_data(**kwargs)
        context['item_form'] = ItemNotaForm
        return context

    def get_success_url(self):
        messages.success(self.request,'Atualizdo com sucesso')
        self.object.total_pedido()
        return reverse_lazy('pedido:nota-update',kwargs = {'pk':self.object.pk})

class AddItemNota(CreateView):
    model = ItemNota
    form_class = ItemNotaForm
    template_name = 'pedido/nota_form.html'
    def form_invalid(self, ItemNotaForm):
        messages.success(self.request,"Ocorreu um problema 'Estoque Insuficiente'.")
        return HttpResponseRedirect(reverse_lazy('pedido:nota-update',kwargs= {'pk':self.request.POST['saida']}))

    def get_success_url(self):
        self.object.nota.total_pedido()
        self.object.produto.atualizaEstoqueAdd(self.object.quantidade)
        return reverse_lazy('pedido:nota-update',kwargs= {'pk':self.object.nota.id})

class DeleteItemNota(View):
    def get(self,request,pk):
        item = ItemNota.objects.get(pk=pk)
        item.produto.atualizaEstoqueRemove(item.quantidade)
        item.delete()
        item.nota.total_pedido()
        messages.success(request,'Item removido')
        return redirect('pedido:nota-update',item.nota.pk)

class UpdateItemNota(UpdateView):
    model = ItemNota
    form_class = ItemNotaForm
    def get_success_url(self):
        self.object.nota.total_pedido()
        return reverse_lazy('pedido:nota-update',kwargs={'pk':self.object.nota.id})

class NotaDetail(View):
    model = Nota


class ConcluirNota(DetailView):

    def get(self,request,pk):
        nota = Nota.objects.get(id=pk)
        nota.concluir_nota()
        messages.success(request,'Nota Concluida')
        return redirect('pedido:nota-update',nota.pk)


class RemoverNota(DetailView):
    def get(self,request,pk):
        nota = Nota.objects.get(id=pk)
        nota.remover_nota()
        messages.success(request,'Nota Removida')
        return redirect('pedido:nota-update',nota.pk)





