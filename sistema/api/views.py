from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import *
from sistema.cadastro.models import *
from sistema.pedido.models import *

class Produtos(ListAPIView):
    serializer_class = SerializerProdutos
    queryset = Produto.objects.all()

class Entradas(ListAPIView):
    serializer_class = SerializerEntradas
    queryset = Nota.objects.all()


class PesquisaProduto(APIView):
    def get(self,request,query):
        contexto = {'request':request}
        queryset = Produto.objects.filter(descricao__icontains=query)
        serializer = SerializerProdutos(queryset,context=contexto,many=True)
        return Response(serializer.data)