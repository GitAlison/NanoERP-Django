from django.urls import path
from .views import *

app_name='api'

urlpatterns = [
    path('produtos',Produtos.as_view(),name='produtos'),
    path('search-produtos/<str:query>',PesquisaProduto.as_view(),name='search-produtos'),

    #Pedidos
    path('entradas',Entradas.as_view(),name='entradas'),
]