from django import forms
from django.core.exceptions import ValidationError
import re
from .models import PerfilUsuario


def validar_telefone(telefone):
    """(XX) XXXX-XXXX"""
    padrao = r'^\(\d{2}\) \d{4}-\d{4}$'
    if not re.match(padrao, telefone):
        raise ValidationError("O telefone deve estar no formato (XX) XXXX-XXXX.")

def validar_cpf(cpf):
    cpf = re.sub(r'\D', '', cpf)  # Remove caracteres não numéricos
    if len(cpf) != 11 or not cpf.isdigit():
        raise ValidationError("CPF inválido. Deve ter 11 dígitos.")
    # Aqui você pode adicionar uma lógica de validação de CPF mais avançada.

def validar_cnpj(cnpj):
    cnpj = re.sub(r'\D', '', cnpj)  # Remove caracteres não numéricos
    if len(cnpj) != 14 or not cnpj.isdigit():
        raise ValidationError("CNPJ inválido. Deve ter 14 dígitos.")
    # Aqui você pode adicionar uma lógica de validação de CNPJ mais avançada.



class LoginForms(forms.Form): 
    nome_login = forms.CharField(
        label="Nome de Login",
        required=True,
        max_length=100,
        widget = forms.TextInput(
            attrs={
                "class": "login-form-group",
                "placeholder": "Digite seu nome",
            }    
        ),
    )
    email = forms.EmailField(
        label="Email",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class": "login-form-group",
                "placeholder": "Digite seu email",
            }
        )
    )
    senha_1 = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget = forms.PasswordInput(
            attrs={
                "class": "login-form-group",
                "placeholder": "Digite sua senha",
            }    
        ),
    )
    senha_2 = forms.CharField(
        label="Confirme a Senha",
        required=True,
        max_length=70,
        widget = forms.PasswordInput(
            attrs={
                "class": "login-form-group",
                "placeholder": "Digite sua senha novamente",
            }    
        ),
    )
    
class CadastroForms(forms.Form):
    class Meta:
        model = PerfilUsuario
        fields = ['telefone', 'data_nascimento', 'tipo_doc', 'documento']
        
    nome_cadastro = forms.CharField(
        label="Nome de Cadastro",
        required=True,
        max_length=100,
        widget = forms.TextInput(
            attrs={
                "class": "registro-form-group",
                "placeholder": "Digite seu nome",
            }    
        ),
    )
    
    email = forms.EmailField(
        label="Email",
        required=True,
        max_length=100,    
        widget=forms.EmailInput(
            attrs={
                "class": "registro-form-group",
                "placeholder": "Digite seu email",
            }
        )
    )
    
    telefone = forms.CharField(
        label="Telefone",
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': '(XX) XXXXX-XXXX', 
                'class': 'registro-form-group'
            }
        ),
        validators=[validar_telefone]
    )
    
    data_nascimento = forms.DateField(
        label="Data de Nascimento",
        required=True,
        widget=forms.DateInput(
            attrs={
            'type': 'date', 
            'class': 'registro-form-group' 
            }
        )
    )
    
    senha_1 = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget = forms.PasswordInput(
            attrs={
                "class": "registro-form-group",
                "placeholder": "Digite sua senha",
            }    
        ),
    )
    
    senha_2 = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget = forms.PasswordInput(
            attrs={
                "class": "registro-form-group",
                "placeholder": "Digite sua senha novamente",
            }    
        ),
    )
    
    tipo_doc = forms.ChoiceField(
        label="Selecione CPF ou CNPJ",
        choices=[
            ('cpf', 'CPF'),
            ('cnpj', 'CNPJ'),
        ],
        widget=forms.Select(
            attrs={
            'class': 'registro-form-group'
            }
        )
    )
    
    documento = forms.CharField(
        label="CPF ou CNPJ",
        required=True,
        max_length=70,
        widget = forms.TextInput(
            attrs={
                "class": "registro-form-group",
                "placeholder": "XXX.XXX.XXXX-XX / XX.XXX.XXX/0001-XX",
            }    
        ),
    )
    
    def clean_documento(self):
        tipo_doc = self.cleaned_data.get('tipo_doc')
        documento = self.cleaned_data.get('documento')
        
        if tipo_doc == 'cpf':
            validar_cpf(documento)
        elif tipo_doc == 'cnpj':
            validar_cnpj(documento)

        return documento
    
    
    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get("nome_cadastro")
        
        if nome:
            nome = nome.strip()
            if " " in nome:
                raise forms.ValidationError("Espaços não são permitidos nesse campo")
            else:
                return nome
        
    def clean_senha_2(self):
        senha_1 = self.cleaned_data.get("senha_1")
        senha_2 = self.cleaned_data.get("senha_2")
            
        if senha_1 and senha_2:
            if senha_1 != senha_2:
                raise forms.ValidationError("Senhas não são iguais")
            else:
                return senha_2
    # email, telefone, data de nascimento, senha, senha2, tipo de documento, cpf ou cnpj e 2 checkbox