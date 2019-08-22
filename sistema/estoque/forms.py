from django import forms
from .models import LocalEstoque,ProdutoEstocado



class LocalEstoqueForm(forms.ModelForm):

    class Meta:
        model = LocalEstoque
        fields = '__all__'
        widgets = {
            'descricao': forms.TextInput(attrs={'class':'form-control'}),
            'produtos_estoque': forms.SelectMultiple(attrs={'class': 'form-control'})
        }



class ProdutoEstocadoForm(forms.ModelForm):

    class Meta:
        model = ProdutoEstocado
        fields = '__all__'