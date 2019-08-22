from django.db import models
from sistema.cadastro.models import Produto
from django.core.validators import MinValueValidator
from decimal import Decimal

DEFAULT_LOCAL_ID = 1

class LocalEstoque(models.Model):
    descricao = models.CharField(max_length=1055)
    produtos_estoque = models.ManyToManyField(Produto, through='estoque.ProdutoEstocado')

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "Local de Estoque"

class ProdutoEstocado(models.Model):
    local = models.ForeignKey(LocalEstoque, related_name="local_produto_estocado",
                              on_delete=models.CASCADE, null=True, blank=True)
    produto = models.ForeignKey(Produto, related_name="produto_estocado",
                                on_delete=models.CASCADE, null=True, blank=True)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2, validators=[
                                     MinValueValidator(Decimal('0.00'))], default=Decimal('0.00'))
