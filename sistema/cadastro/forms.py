from django import forms
from .models import Cliente,Funcionario,Produto,Categoria,Unidade,Fornecedor,FornecedorProduto

#TODO Formulario cadastro de cliente
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'nome':forms.TextInput(attrs={'class':'form-control'}),
            'rg_ie': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf_cnpj': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_pessoa': forms.Select(attrs={'class': 'form-control select2'}),
            'fixo': forms.TextInput(attrs={'class': 'form-control'}),
            'whatsapp': forms.TextInput(attrs={'class': 'form-control'}),
            'celular': forms.TextInput(attrs={'class': 'form-control'}),
            'trabalho': forms.TextInput(attrs={'class': 'form-control'}),
            'logradouro': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'uf': forms.TextInput(attrs={'class': 'form-control'}),
            'cep': forms.TextInput(attrs={'class': 'form-control'}),
        }

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = '__all__'
        widgets = {
            'nome':forms.TextInput(attrs={'class':'form-control'}),
            'rg_ie': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf_cnpj': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_pessoa': forms.Select(attrs={'class': 'form-control select2'}),
            'fixo': forms.TextInput(attrs={'class': 'form-control'}),
            'whatsapp': forms.TextInput(attrs={'class': 'form-control'}),
            'celular': forms.TextInput(attrs={'class': 'form-control'}),
            'trabalho': forms.TextInput(attrs={'class': 'form-control'}),
            'logradouro': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'uf': forms.TextInput(attrs={'class': 'form-control'}),
            'cep': forms.TextInput(attrs={'class': 'form-control'}),
        }


class FuncionarioForm(forms.ModelForm):
    salario = forms.DecimalField(label='Salário',localize=True,max_digits=10,decimal_places=2,
                                 widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Funcionario
        fields = ['nome','rg_ie','cpf_cnpj','data_nascimento','data_admissao','data_demissao','salario','tipo_pessoa']
        widgets = {
            'nome':forms.TextInput(attrs={'class':'form-control'}),
            'rg_ie': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf_cnpj': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_pessoa': forms.Select(attrs={'class': 'form-control select2'}),
            'data_nascimento': forms.TextInput(attrs={'class': 'form-control','type':'date'}),
            'data_admissao': forms.TextInput(attrs={'class': 'form-control','type':'date'}),
            'data_demissao': forms.TextInput(attrs={'class': 'form-control','type':'date'})
        }


class ProdutoForm(forms.ModelForm):
    preco = forms.DecimalField(label='Preço', localize=True,max_digits=10,decimal_places=2,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    custo = forms.DecimalField(label='Custo',localize=True,max_digits=10,decimal_places=2,
                               widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Produto
        fields = '__all__'
        widgets = {
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control select2 '}),
            'unidade': forms.Select(attrs={'class': 'form-control select2'}),
            'fornecedor': forms.Select(attrs={'class': 'form-control select2'}),
            'controle_estoque': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'fora_de_linha': forms.CheckboxInput(attrs={'class': ''}),
            'estoque_minimo': forms.TextInput(attrs={'class': 'form-control','type':'number'}),
            'estoque_atual': forms.TextInput(attrs={'class': 'form-control','type':'number'}),

            'cod_barras': forms.TextInput(attrs={'class': 'form-control'}),

            'DELETE': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = '__all__'
        widgets = {
            'nome':forms.TextInput(attrs={'class':'form-control'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
        }

class UnidadeForm(forms.ModelForm):

    class Meta:
        model = Unidade
        fields = '__all__'
        widgets = {
            'sigla':forms.TextInput(attrs={'class':'form-control'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
        }



class FornecedorProdutoForm(forms.ModelForm):

    class Meta:
        model = FornecedorProduto
        fields = '__all__'
        widgets = {
            'fornecedor': forms.Select(attrs={'class':'form-control select2'}),
            'unidade': forms.Select(attrs={'class': 'form-control select2'}),
            'quantidade': forms.TextInput(attrs={'class': 'form-control','type':'number'}),
            'DELETE': forms.CheckboxInput(attrs={'class': 'form-control bg-primary'}),
        }

FornecedorProdutoFormSet = forms.inlineformset_factory(Produto,FornecedorProduto,form=FornecedorProdutoForm,extra=2,can_delete=True)
