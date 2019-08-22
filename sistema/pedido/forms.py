from django import forms
from .models import Nota,ItemNota
from sistema.cadastro.models import Produto,FornecedorProduto


class NotaForm(forms.ModelForm):

    total = forms.DecimalField(label="Total do pedido",max_digits=10,decimal_places=2,
                               localize=True,required=False,
                               widget=forms.TextInput(attrs={'class':'form-control bg-success text-light'}))
    desconto = forms.DecimalField(label="Desconto do pedido", max_digits=10, decimal_places=2,
                               localize=True,required=False,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    despesa = forms.DecimalField(label="Despesa do pedido", max_digits=10, decimal_places=2,
                               localize=True,required=False,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean(self):
        desconto = self.cleaned_data['desconto'] or 0
        total = self.cleaned_data['total'] or 0
        print(desconto)
        print(total)
        if self.cleaned_data['total']:
            if float(desconto) > float(total):
                raise forms.ValidationError('Desconto não pode ser maior que o valor do pedido')


    class Meta:
        model = Nota
        fields = ['tipo','numero','serie','chave','cliente','funcionario','data_emissao','total','desconto','despesa']
        widgets = {
            'tipo':forms.Select(attrs={'class':'form-control select2'}),
            'numero':forms.TextInput(attrs={'class':'form-control'}),
            'serie':forms.TextInput(attrs={'class':'form-control'}),
            'chave':forms.TextInput(attrs={'class':'form-control'}),
            'cliente':forms.Select(attrs={'class':'form-control select2'}),
            'funcionario': forms.Select(attrs={'class': 'form-control select2'}),
            'data_emissao': forms.TextInput(attrs={'class': 'form-control','type':'date'})
        }



class ItemNotaForm(forms.ModelForm):

    quantidade = forms.DecimalField(label="Quantidade", max_digits=10, decimal_places=2,
                               localize=True, required=False,
                               widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
    valor_unitario = forms.DecimalField(label="Valor Unit.", max_digits=10, decimal_places=2,
                                  localize=True, required=False,
                                  widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
    desconto_item = forms.DecimalField(label="Desconto", max_digits=10, decimal_places=2,
                                 localize=True, required=False,
                                 widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
    total_item = forms.DecimalField(label="Total Item", max_digits=10, decimal_places=2,
                                  localize=True, required=False,
                                  widget=forms.TextInput(attrs={'class': 'form-control form-control-sm','readonly':'true'}))

    # def clean(self):
    #     quantidade = self.cleaned_data['quantidade']
    #     produto_data = self.cleaned_data['produto']
    #     produto = Produto.objects.get(id=produto_data.id)
    #     estoque = produto.estoque()
    #     if quantidade > estoque:
    #         raise forms.ValidationError('O estoque não é suficiente'+str(estoque))


    class Meta:
        model = ItemNota
        fields = ['nota','produto','quantidade','valor_unitario','desconto_item','total_item']
        widgets ={
            'produto':forms.Select(attrs={'class':'form-control select2'})
        }

