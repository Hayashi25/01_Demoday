from django import forms
from .models import Escola, Aluno, Parceiro
from website.choices import REDES_ENSINO, TIPOS_ENSINO, TIPO_PARCERIA

class CadastroEscola(forms.ModelForm):
    class Meta:
        model = Escola
        fields = ('nome_escola', 'endereco_escola', 'telefone_escola', 'email',
                  'rede_ensino', 'tipo_ensino', 'codigo_acesso', 'senha_acesso')
        widgets = {
            'nome_escola': forms.TextInput(attrs={'required': True, 'id': 'nome_escola'}),
            'endereco_escola': forms.TextInput(attrs={'required': True, 'id': 'endereco_escola'}),
            'telefone_escola': forms.NumberInput(attrs={'required': True, 'id': 'telefone_escola'}),
            'email': forms.EmailInput(attrs={'required': True, 'id': 'email'}),
            'rede_ensino': forms.Select(choices=REDES_ENSINO, attrs={'required': True, 'id': 'rede_ensino'}),
            'tipo_ensino': forms.Select(choices=TIPOS_ENSINO, attrs={'required': True, 'id': 'tipos_ensino'}),
            'codigo_acesso': forms.TextInput(attrs={'required': True, 'id': 'codigo_acesso'}),
            'senha_acesso': forms.PasswordInput(attrs={'required': True, 'id': 'senha_acesso'}),
        }

class CadastrarParceiros(forms.ModelForm):
    class Meta:
        model = Parceiro
        fields = ('tipo_parceiro', 'nome_parceiro', 'email_parceiro', 'telefone_parceiro', 'mensagem_parceiro')
        widgets = {
            'tipo_parceiro': forms.Select(choices=TIPO_PARCERIA, attrs={'required': True, 'id': 'tipo_parceiro'}),
            'nome_parceiro': forms.TextInput(attrs={'required': True, 'id': 'nome_parceiro'}),
            'email_parceiro': forms.EmailInput(attrs={'required': True, 'id': 'email_parceiro'}),
            'telefone_parceiro': forms.NumberInput(attrs={'required': True, 'id': 'telefone_parceiro'}),
            'mensagem_parceiro': forms.TextInput(attrs={'required': True, 'id': 'mensagem_parceiro'}),
        }

