from rest_framework.serializers import ModelSerializer
from sistema.cadastro.models import *
from sistema.pedido.models import *

class SerializerProdutos(ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(SerializerProdutos, self).to_representation(instance)
        representation['fornecedor'] = instance.fornecedor.nome or None
        representation['categoria'] = instance.categoria.descricao or None
        representation['unidade'] = instance.unidade.sigla or None
        return representation


class SerializerEntradas(ModelSerializer):

    class Meta:
        model = Nota
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(SerializerEntradas, self).to_representation(instance)
        representation['fornecedor'] = instance.fornecedor.nome
        representation['funcionario'] = instance.funcionario.nome
        return representation
