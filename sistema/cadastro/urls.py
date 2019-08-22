from django.urls import path
from . import views

app_name = 'cadastro'
urlpatterns = [
    #TODO API
    path('produtoApi/<int:id>/',views.ProdutoApi.as_view(),name='produto_api'),
    path('clienteApi/',views.ClienteApi.as_view(),name='cliente_api'),

    # TODO url Produto
    path('produto',views.ProdutoCreate,name='produto'),
    path('produtos', views.ProdutoList.as_view(), name='produto-list'),
    path('produto-update/<int:pk>/', views.ProdutoUpdate, name='produto-update'),
    # TODO url Categoria
    path('categoria', views.CategoriaCreate.as_view(), name='categoria'),
    path('categorias', views.CategoriaList.as_view(), name='categoria-list'),
    path('categoria-update/<int:pk>/', views.CategoriaUpdate.as_view(), name='categoria-update'),
    # TODO url Unidade
    path('unidade', views.UnidadeCreate.as_view(), name='unidade'),
    path('unidades', views.UnidadeList.as_view(), name='unidade-list'),
    path('unidade-update/<int:pk>/', views.UnidadeUpdate.as_view(), name='unidade-update'),
    # TODO url Cliente
    path('cliente', views.ClienteCreate.as_view(), name='cliente'),
    path('clientes', views.ClienteList.as_view(), name='cliente-list'),
    path('cliente-update/<int:pk>/', views.ClienteUpdate.as_view(), name='cliente-update'),
    # TODO url Funcionario
    path('funcionario', views.FuncionarioCreate.as_view(), name='funcionario'),
    path('funcionarios', views.FuncionarioList.as_view(), name='funcionario-list'),
    path('funcionario-update/<int:pk>/', views.FuncionarioUpdate.as_view(), name='funcionario-update'),
    # TODO url Fornecedor
    path('fornecedor', views.FornecedorCreate.as_view(), name='fornecedor'),
    path('fornecedores', views.FornecedorList.as_view(), name='fornecedor-list'),
    path('fornecedor-update/<int:pk>/', views.FornecedorUpdate.as_view(), name='fornecedor-update')
]
