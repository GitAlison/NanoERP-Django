from rest_framework.serializers import ModelSerializer
from .models import Produto,Cliente

class ProdutoSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = ['descricao','preco']


class ClienteSerializer(ModelSerializer):

    class Meta:
        model = Cliente
        fields = '__all__'

    