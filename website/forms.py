from django import forms
from .models import Escola, Aluno, Contato
from website.choices import REDES_ENSINO, TIPOS_ENSINO

class CadastroEscola(forms.ModelForm):
    class Meta:
        model = Escola
        fields = ('nome_escola', 'endereco_escola', 'diretor_responsavel', 'email',
                  'rede_ensino', 'tipo_ensino', 'codigo_acesso', 'senha_acesso', 'confirmar_senha')
        widgets = {
            'nome_escola': forms.TextInput(attrs={
                'required': True,
                'id': 'nome_escola'}),

            'endereco_escola': forms.TextInput(attrs={
                'required': True,
                'id': 'endereco_escola'}),

            'diretor_responsavel': forms.TextInput(attrs={
                'required': True,
                'id': 'diretor_responsavel'}),

            'email': forms.EmailInput(attrs={
                'required': True,
                'id': 'email'}),

            'rede_ensino': forms.Select(choices=REDES_ENSINO, attrs={
                'required': True,
                'id': 'rede_ensino'}),

            'tipo_ensino': forms.Select(choices=TIPOS_ENSINO, attrs={
                'required': True,
                'id': 'tipos_ensino'}),

            'codigo_acesso': forms.TextInput(attrs={
                'required': True,
                'id': 'codigo_acesso'}),
        
            'senha_acesso': forms.PasswordInput(attrs={
                'required': True,
                'id': 'senha_acesso'}),

            'confirmar_senha': forms.PasswordInput(attrs={
                'required': True,               
                'id': 'confirmar_senha'}), 
        }

    def clean(self):
        cleaned_data = super(CadastroEscola, self).clean()
        senha_acesso = cleaned_data.get('senha_acesso')

        tamanho_minimo = 8
        if len(senha_acesso) < tamanho_minimo:
            msg = 'A senha deve ter pelo menos %s caracteres.' %(str(tamanho_minimo))
            self.add_error('senha_acesso', msg)

        confirmar_senha = cleaned_data.get('confirmar_senha')
        if senha_acesso and confirmar_senha:
            if senha_acesso != confirmar_senha:
                msg = 'As duas senhas devem corresponder.'
                self.add_error('confirmar_senha', msg)
        return cleaned_data


class ContatarPessoas(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ('from_email', 'subject', 'message')
        widgets = {
            'subject': forms.TextInput(attrs={
                'required': True,
                'id': 'subject'}),

            'from_email': forms.EmailInput(attrs={
                'required': True,
                'id': 'from_email'}),

            'message': forms.Textarea(attrs={
                'required': True,
                'id': 'message'}),
        }