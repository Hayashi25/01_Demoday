from django import forms
from .models import Escola, Aluno, Parceiro
from website.choices import REDES_ENSINO, TIPOS_ENSINO

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
