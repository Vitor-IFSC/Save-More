from django import forms
from .models import Compra

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['nome_item', 'preco', 'endereco', 'quantidade', 'numero_contato', 'foto_item', 'instituicao']
