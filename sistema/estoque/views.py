from django.shortcuts import render
from django.contrib import messages
from django.views.generic import View,ListView
from django.views.generic.edit import CreateView,UpdateView,ModelFormMixin
from .models import LocalEstoque,ProdutoEstocado
from .forms import LocalEstoqueForm
msg_success = 'Registro inserido'
msg_update = 'Registro Atualizado'


#TODO Local Estoque View

class EstoqueList(ListView):
    model = LocalEstoque

class EstoqueCreate(CreateView):
    model = LocalEstoque
    form_class = LocalEstoqueForm
    def get_success_url(self):
        messages.success(self.request,msg_success)

class EstoqueUpdate(UpdateView):
    model = LocalEstoque
    form_class = LocalEstoqueForm
    def get_success_url(self):
        messages.success(self.request,msg_update)