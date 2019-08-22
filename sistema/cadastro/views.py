from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView,View
from django.views.generic.edit import CreateView,UpdateView
from django.contrib import messages
from .forms import ClienteForm,FuncionarioForm,FornecedorForm,ProdutoForm,CategoriaForm,UnidadeForm,FornecedorProdutoFormSet
from .models import Cliente,Funcionario,Fornecedor,Produto,Categoria,Unidade
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,CreateAPIView,ListCreateAPIView
from .serializers import ProdutoSerializer,ClienteSerializer

msg_success = 'Registro inserido'
msg_update = 'Registro Atualizado'

# TODO API View
class ProdutoApi(APIView):
    def get(self,request,id):
        produtos = Produto.objects.filter(id=id,fora_de_linha=False)
        contexto = ('request', request)
        serializer = ProdutoSerializer(produtos,context=contexto,many=True)
        return Response(serializer.data)

class ClienteApi(ListCreateAPIView):
    queryset = Cliente.objects.all()
    model = Cliente
    serializer_class = ClienteSerializer

# TODO PRODUTO
class ProdutoList(ListView):
    model = Produto
    def get_queryset(self):
        return Produto.objects.all()#[:5]


def ProdutoCreate(request):

    template_name = 'cadastro/produto_form.html'
    produto = Produto()
    form = ProdutoForm(request.POST or None,instance=produto)
    fornecedorformset = FornecedorProdutoFormSet(request.POST or None,instance=produto)

    if form.is_valid() and fornecedorformset.is_valid():
        form.save()
        fornecedorformset.save()
        messages.success(request,'Registrado')

        return redirect('cadastro:produto-list')

    contexto = {
        'form':form,
        'fornecedor_formset':fornecedorformset
    }
    return render(request,template_name,contexto)


def ProdutoUpdate(request,pk):
    template_name = 'cadastro/produto_form.html'
    produto = Produto.objects.get(pk=pk)
    form = ProdutoForm(request.POST or None, instance=produto)
    fornecedorformset = FornecedorProdutoFormSet(request.POST or None, instance=produto)

    if form.is_valid() and fornecedorformset.is_valid():
        form.save()
        fornecedorformset.save()
        messages.success(request,'Atualizado')
        return redirect('cadastro:produto-list')

    contexto = {
        'form': form,
        'fornecedor_formset': fornecedorformset
    }
    return render(request, template_name, contexto)
    # model = Produto
    # form_class = ProdutoForm
    # def get_context_data(self, **kwargs):
    #     context = super(ProdutoUpdate,self).get_context_data(**kwargs)
    #     context['fornecedor_formset'] = FornecedorProdutoFormSet(self.request.POST or None, instance=self.object,prefix='fornecedor')
    #     return context
    #
    #
    # def get_success_url(self):
    #     messages.success(self.request,msg_update)
    #     return reverse_lazy('cadastro:produto-list')


# TODO Categoria
class CategoriaList(ListView):
    model = Categoria

class CategoriaCreate(CreateView):
    model = Categoria
    form_class = CategoriaForm
    def get_success_url(self):
        messages.success(self.request,msg_success)
        return reverse_lazy('cadastro:categoria-list')



class CategoriaUpdate(UpdateView):
    model = Categoria
    form_class = CategoriaForm
    def get_success_url(self):
        messages.success(self.request,msg_update)
        return reverse_lazy('cadastro:categoria-list')


# TODO Unidade
class UnidadeList(ListView):
    model = Unidade

class UnidadeCreate(CreateView):
    model = Unidade
    form_class = UnidadeForm
    def get_success_url(self):
        messages.success(self.request,msg_success)
        return reverse_lazy('cadastro:unidade-list')

class UnidadeUpdate(UpdateView):
    model = Unidade
    form_class = UnidadeForm
    def get_success_url(self):
        messages.success(self.request,msg_update)
        return reverse_lazy('cadastro:unidade-list')


# TODO Cliente
class ClienteList(ListView):
    model = Cliente

class ClienteCreate(CreateView):
    model = Cliente
    form_class = ClienteForm
    def get_success_url(self):
        messages.success(self.request,msg_success)
        return reverse_lazy('cadastro:cliente-list')

class ClienteUpdate(UpdateView):
    model = Cliente
    form_class = ClienteForm

    def get_success_url(self):
        messages.success(self.request,msg_update)
        return reverse_lazy('cadastro:cliente-list')

# TODO Funcionario
class FuncionarioList(ListView):
    model = Funcionario

class FuncionarioCreate(CreateView):
    model = Funcionario
    form_class = FuncionarioForm
    def get_success_url(self):
        messages.success(self.request,msg_success)
        return reverse_lazy('cadastro:funcionario-list')

class FuncionarioUpdate(UpdateView):
    model = Funcionario
    form_class = FuncionarioForm
    def get_success_url(self):
        messages.success(self.request,msg_update)
        return reverse_lazy('cadastro:funcionario-list')

# TODO Fornecedor
class FornecedorList(ListView):
    model = Fornecedor

class FornecedorCreate(CreateView):
    model = Fornecedor
    form_class = FornecedorForm
    def get_success_url(self):
        messages.success(self.request,msg_success)
        return reverse_lazy('cadastro:fornecedor-list')

class FornecedorUpdate(UpdateView):
    model = Fornecedor
    form_class = FornecedorForm
    def get_success_url(self):
        messages.success(self.request,msg_update)
        return reverse_lazy('cadastro:fornecedor-list')


