from django import forms
from .models import Escola, Aluno, Parceiro

class CadastroEscola(forms.ModelForm):
    class Meta:
        model = Escola
        fields = ('nome_escola', 'endereco_escola', 'telefone_escola',
                  'email_escola', 'rede_ensino', 'tipo_ensino',
                  'codigo_acesso', 'senha_acesso')